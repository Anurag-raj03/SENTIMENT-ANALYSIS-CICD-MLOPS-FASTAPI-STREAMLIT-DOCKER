import os
import pandas as pd
import sys  
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from STEPS.data_reading import read_f
from preprocess.labeling import labe
from preprocess.remove_espace import removesp
from preprocess.removing_link import removing_links
from preprocess.remving_string import remove_unwanted_strings
from preprocess.making_lowerCase import preprocess_text
from preprocess.removing_no import rem_number
from preprocess.steme import apply_snowball_stemming_g
from preprocess.dropping_na import drop_in
from preprocess.resampl import balance_classes
from model_making.model_trainig import model_building
from model_making.splitin_x_y import split_x_y
from model_making.word_vec import vec_conv



logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_pipeline():
    try:
        logging.info("READING THE DATASET.....")
        file_path = os.path.abspath("DATA/data.csv")

        df = read_f(file_path)
        if df is None:
            raise ValueError("FAILED TO LOAD THE DATASET")
        
        logging.info("PREPROCESSING OF THE DATA")
        
        df=removing_links(df)
        df=rem_number(df)
        df=remove_unwanted_strings(df)
        df=removesp(df)
        df=preprocess_text(df)
        df=apply_snowball_stemming_g(df,column_name='Sentence')
        df.to_csv("make.csv")
        df=balance_classes(df)
        new_path="DATA/data_modified.csv"
        
        df=pd.read_csv(new_path)
        df=labe(df)
        
        
        logging.info("Model Making Process start from here")
        logging.info("Data Splitting into trian test")
        x_train,x_test,y_train,y_test=split_x_y(df,col='Sentence',tar='Sentiment',random_state=42,test_split=0.2)
        logging.info("Converting text to numerical vectors (TF-IDF)...")
        x_tfidf, y_train = vec_conv(x_train, y_train, save_path="Save_model/tf_vectorizer.jbl")

        logging.info("Training the model...")
        accuracy = model_building(x_tfidf, y_train, x_test, y_test, vectorizer_path="Save_model/tf_vectorizer.jbl", save_path="Save_model/extra_trees.jbl")

        logging.info(f"Pipeline completed successfully with model accuracy: {accuracy:.2f}%")
        
        
        
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except KeyError as e:
        logging.error(f" Missing column in dataset: {e}")
    except ValueError as e:
        logging.error(f"Value Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected Error: {e}")

if __name__ == "__main__":
    run_pipeline()