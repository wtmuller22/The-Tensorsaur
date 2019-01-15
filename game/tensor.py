'''
Created on Dec 31, 2018

@author:  cpendery, wmuller
'''


import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import metrics
from tensorflow.python.data import Dataset
import math

distance_file = open("logs/distanceToObstacle.txt", 'r')
result_1 = [line.split(',') for line in distance_file]
height_file = open("logs/heightOfObstacle.txt", 'r')
result_2 = [line.split(',') for line in height_file]
width_file = open("logs/widthOfObstacle.txt", 'r')
result_3 = [line.split(',') for line in width_file]
obstacle_y_file = open("logs/obstacleYPosition.txt", 'r')
result_4 = [line.split(',') for line in obstacle_y_file]
speed_file = open("logs/speed.txt", 'r')
result_5 = [line.split(',') for line in speed_file]
player_y_file = open("logs/playerYPosition.txt", 'r')
result_6 = [line.split(',') for line in player_y_file]
gap_file = open("logs/gapBetweenObstacles.txt", 'r')
result_7 = [line.split(',') for line in gap_file]
state_file = open("logs/playerState.txt", 'r')
result_8 = [line.split(',') for line in state_file]


#Gets rid of last empty element due to end commas
del result_1[0][-1]
del result_2[0][-1]
del result_3[0][-1]
del result_4[0][-1]
del result_5[0][-1]
del result_6[0][-1]
del result_7[0][-1]
del result_8[0][-1]


#7 params
#{distance to ob, height of ob, width of ob, bird height, speed, player y pos, gap between obs}
#3 lables
#0 = stay, 1 = jump, 2 = duck
distance_to = pd.Series([float(num) for num in result_1[0]])
height_of = pd.Series([float(num) for num in result_2[0]])
width_of = pd.Series([float(num) for num in result_3[0]])
obstacle_y = pd.Series([float(num) for num in result_4[0]])
speed = pd.Series([float(num) for num in result_5[0]])
player_y = pd.Series([float(num) for num in result_6[0]])
obstacle_gap = pd.Series([float(num) for num in result_7[0]])
labels = pd.Series([int(num) for num in result_8[0]])

playing_data = pd.DataFrame({ 'distance_to_obstacle': distance_to, 'height_of_obstacle': height_of,
                             'width_of_obstacle': width_of, 'obstacle_y_position': obstacle_y, 
                             'speed': speed, 'player_y_position': player_y, 
                             'gap_between_obstacles': obstacle_gap, 'player_state': labels})
#print(playing_data)

def make_prediction(features):
    prediction = linear_classifier.predict(features) 
    return prediction

#Randomizes data to help SGD
playing_data = playing_data.reindex(np.random.permutation(playing_data.index))

def preprocess_features(playing_data):
    selected_features = playing_data[["distance_to_obstacle", "height_of_obstacle", 
                                      "width_of_obstacle", "obstacle_y_position", "speed", "player_y_position",
                                      "gap_between_obstacles"]]
    processed_features = selected_features.copy()
    return processed_features

def preprocess_targets(playing_data):
    output_targets = pd.DataFrame()
    output_targets["player_state"] = playing_data["player_state"]
    return output_targets

training_examples = preprocess_features(playing_data.head(5009))
training_targets = preprocess_targets(playing_data.head(5009))
validation_examples = preprocess_features(playing_data.tail(1000))
validation_targets = preprocess_targets(playing_data.tail(1000))

def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    features = {key:np.array(value) for key,value in dict(features).items()}
    ds = Dataset.from_tensor_slices((features, targets))
    ds = ds.batch(batch_size).repeat(num_epochs)
    if shuffle:
        ds = ds.shuffle(10000)
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

def construct_feature_columns(input_features):
    return set([tf.feature_column.numeric_column(my_feature) for my_feature in input_features])

def train_model(learning_rate, steps, batch_size, training_examples, training_targets, validation_examples, validation_targets):
    periods = 10
    steps_per_period = steps / periods
    
    my_optimizer = tf.train.AdagradOptimizer(learning_rate=learning_rate)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
    linear_classifier = tf.estimator.LinearClassifier(feature_columns=construct_feature_columns(training_examples),
                                                    optimizer=my_optimizer, n_classes=3, 
                                                    config=tf.estimator.RunConfig(keep_checkpoint_max=1))
    
    training_input_fn = lambda: my_input_fn(training_examples, training_targets["player_state"], batch_size=batch_size)
    predict_training_input_fn = lambda: my_input_fn(training_examples, training_targets["player_state"], shuffle=False, num_epochs=1)
    predict_validation_input_fn = lambda: my_input_fn(validation_examples, validation_targets["player_state"], shuffle=False, num_epochs=1)
    
    print("Training in Progress...")
    print("LogLoss (training data):")
    training_log_losses = []
    validation_log_losses = []
    for period in range(0, periods):
        linear_classifier.train(input_fn=training_input_fn, steps=steps_per_period)
        
        training_predictions = list(linear_classifier.predict(input_fn=predict_training_input_fn))
        training_probabilities = np.array([item['probabilities'] for item in training_predictions])
        training_pred_class_id = np.array([item['class_ids'][0] for item in training_predictions])
        training_pred_one_hot = tf.keras.utils.to_categorical(training_pred_class_id,3)
            
        validation_predictions = list(linear_classifier.predict(input_fn=predict_validation_input_fn))
        validation_probabilities = np.array([item['probabilities'] for item in validation_predictions])    
        validation_pred_class_id = np.array([item['class_ids'][0] for item in validation_predictions])
        validation_pred_one_hot = tf.keras.utils.to_categorical(validation_pred_class_id,3)
        
        training_log_loss = metrics.log_loss(training_targets, training_pred_one_hot)
        validation_log_loss = metrics.log_loss(validation_targets, validation_pred_one_hot)
        print("Period %02d : %0.2f" % (period, training_log_loss))
        print("Validation: %0.2f" % (validation_log_loss))
        training_log_losses.append(training_log_loss)
        validation_log_losses.append(validation_log_loss)
    print("Model Training Complete.")
    
    final_predictions = linear_classifier.predict(input_fn=predict_validation_input_fn)
    final_predictions = np.array([item['class_ids'][0] for item in final_predictions])
    
    accuracy = metrics.accuracy_score(validation_targets, final_predictions)
    print("Final accuracy (validation data): %0.2f" % accuracy)
    
    return linear_classifier

#train model

linear_classifier = train_model(learning_rate=0.0002,
                                steps=3000, 
                                batch_size=30,
                                training_examples=training_examples, 
                                training_targets=training_targets, 
                                validation_examples=validation_examples, 
                                validation_targets=validation_targets)
