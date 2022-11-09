import tensorflow as tf
import tensorflow_hub as hub
# To find out cosine similarity, we will use the following libraries
import numpy as np
from numpy.linalg import norm

url = "https://tfhub.dev/google/universal-sentence-encoder/4" #Model is imported from this URL
model = hub.load(url)

def embedding(input):
  return model(input)


def find_sim(t1, t2):
  # msg = [df['text1'][i], df['text2'][i]]
  msg = [t1, t2]
  msg_emb = embedding(msg)
  # Making numpy array out of the embedding output
  x = tf.make_ndarray(tf.make_tensor_proto(msg_emb))
  cos_sim = np.dot(x[0], x[1])/(norm(x[0])*norm(x[1]))
  # Scaling the cosine similarity between 0 and 1
  cos_sim = (cos_sim + 1)/2
  dict = {}
  dict.update({'similarity score': cos_sim})
  # cosine_similarity = pd.DataFrame(cos_list, columns = ['Similarity'])
  # # Range of cosine similarity output is from -1 to 1. We add one and normalize it to fall in the range of 0 to 1
  # cosine_similarity = cosine_similarity + 1
  # cosine_similarity = cosine_similarity/cosine_similarity.abs().max() #Normalizing the Similarity_Score to get the value between 0 and 1
  # print(cosine_similarity.head())
  return dict