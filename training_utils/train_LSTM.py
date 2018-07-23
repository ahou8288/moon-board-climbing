import os
# surpress tesnsorflow warning
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys

# import LSTM model
network_folder = '{}/models/char-rnn-tensorflow/'.format(base_directory)
sys.path.append(network_folder)
import train


def train_model(grade_mode):
    # Check that function parameters are valid
    if not grade_mode in ['no_grade', 'post_grade', 'pre_grade']:
        raise ValueError(
            'Invalid grade_mode for model training. Use no_grade, post_grade or pre_grade as the grade_mode parameter.')

    # Find directories
    base_save_dir = '{}/data/lstm_files/{}/'.format(base_directory, grade_mode)

    # Train the model
    train.build_model(base_save_dir)

if __name__ == '__main__':
    grade_mode = 'no_grade'
    train_model(grade_mode)
