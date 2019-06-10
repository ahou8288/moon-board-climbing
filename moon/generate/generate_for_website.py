from moon.utils.load_data import load_climbset, local_file_path
from moon.models import keras_lstm_gen
import pickle


def main():
    # Load climbset
    climbset = load_climbset("2016")

    # Sample generators
    lstm = keras_lstm_gen.Model()
    
    # Save to file
    file_data ={
        "original": climbset,
        "lstm": lstm.sample(climbset, 500, maxlen=12, epochs=1),
    }

    print(f"Saving {len(file_data)} climbsets")
    pickle.dump(file_data, open(local_file_path(__file__, "climbsets.pickle"), "wb"))


if __name__=="__main__":
    main()
