import requests
import os
import pandas as pd
import json
import pickle


def save_new_chain(user_query, output_chain, answer):
    try:
        df = pd.read_csv('./data/chains.csv', index_col=0)
        df.loc[len(df)] = {'query':user_query, 'chain':output_chain, 'answer': answer}
        df.to_csv('./data/chains.csv')

    except FileNotFoundError:
        df = pd.DataFrame([[user_query, output_chain, answer]])
        df.columns = ['query', 'chain', 'answer']
        df.to_csv('./data/chains.csv')

def get_last_chains(how_many=5):
    try:
        df = pd.read_csv('./data/chains.csv', index_col=0)
        return df.tail(how_many)
    except:
        return ''