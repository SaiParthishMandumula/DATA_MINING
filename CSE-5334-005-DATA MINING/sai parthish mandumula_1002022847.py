

import nltk #importing natural language took kit.
import math #importing math function for math calculations.
import os #importing operating system for the task to do.
from nltk.tokenize import RegexpTokenizer #from the  nltk.tokenize functions we import regexptokenizer  to import the token range.
from nltk.corpus import stopwords #nltk,corpus we need to import  the stop words to do the task.
from nltk.stem.porter import PorterStemmer#from the nltk.stem.porter we need to import porterstemmer where we need pass the common
#string the branches will come.
from math import log10#from math lib we will import the log10 function
from math import sqrt#from the math lib we will  import the sqrt for the square root equations.
from collections import Counter#we need to import the counter to count the collections.
stemmer = PorterStemmer()#we decalre the stemmer to count the branches for the common words.
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')#tokenizer where we give tokens  to the rengexptokenier  that we import from the inbuilt function.
corpusroot = './presidential_debates'# ./presidential_debates  is the file given.
string_sequence_vector={}       #e_vector needed to be decalred .
string_sequence_frequency=Counter()          # we need to count the frequency where we will count the no of elements.
token_frequencies={}             #we decalre the  ies to be null for the functions.
computed_length=Counter()     #we initializing the counter value to h.
computed_list_info={}     #we need to find the info for the above equaqtion.
st_tokens=[] ## we decalre the string tokens for the tokens to initializing the giving task.

for targetfile in os.listdir(corpusroot):#for the targetfile  we need to run with os to get the list  of the corpusroot.
    openedfile = open(os.path.join(corpusroot, targetfile), "r", encoding='UTF-8')## we need to open the file where path need to get connected.
    tolower_string = openedfile.read()#we open the file and the read  the file to run  where we initializing the tolower_string.
    openedfile.close()#we need to close the file that is opened.
    tolower_string = tolower_string.lower()#we need to lower  the string in the file.
    target_token = tokenizer.tokenize(tolower_string) # there should not be there any alphabetical difference between captial and small.
    stopword_list=stopwords.words('english')#we need to have the stopwords for the english alphabets.
    target_token = [stemmer.stem(token) for token in target_token if token not in stopword_list]#we stemmer the stem of the token
    #where the target_tokenvalue   need to take for the stopwords in list.
    ticket_frequency=Counter(target_token)#for the ticket_frequency we need to count the target_tokenvalue.
    string_sequence_frequency+=Counter(list(set(target_token)))# for the string sequence frequency increment to the counter list.
    # where the sets the target value for  tokens.
    token_frequencies[targetfile]=ticket_frequency.copy()#we copy the string where the tokens are needed to given the tickets and copy the file.
    ticket_frequency.clear()# where we clear the ticket frequency .


def compute_intermittiant_weight(targetfile, token):# for the compute intermittiant weigth we decalre the target file and tokens.
    freuencies_of_id=getidf(token) #we declare the functions  with the id and we get the getid tokens.
    return (1+log10(token_frequencies[targetfile][token]))*freuencies_of_id# we return  value.

def getidf(token):# we decalre the getidf where the tokens
    if string_sequence_frequency[token]==0:# if the strings sequence frequency of the tokens to 0.
        return -1## we decalre the return the less than 1 function.
    return log10(len(token_frequencies)/string_sequence_frequency[token])#  we return the log10 to len the token frquency   divide byt the  string sequence  frequency.

#loop for calculating tf-idf string_sequence_vector and lengths of documents
for targetfile in token_frequencies:# we take the targetfile in the token frequencies.
    string_sequence_vector[targetfile]=Counter() # we decalre the string sequence vector to the target file with  the counter.
    string_sequence_size=0 #we decalre the string sequence size with 0.
    for token in token_frequencies[targetfile]:# for the token in token frequency with the targetfile .
        normalized_string_weight = compute_intermittiant_weight(targetfile, token) #we decalre the normalized string weight equals compute the.
        #intermittiant_weigth  with the targetfile and the tokens .
        string_sequence_vector[targetfile][token] = normalized_string_weight # we decalre the string sequence vector  wit the
        # with the product of the  targetfile and token so we get the normalized_string_weight.
        string_sequence_size += normalized_string_weight**2#we increment the string_sequence_size to double the normalized_string_weight
    computed_length[targetfile]=math.sqrt(string_sequence_size)#we compute the length with the math.sqrt of the string_sequence_size.

# we make the loop  to make the normalized.
for targetfile in string_sequence_vector: # for the targetfile in string_sequence_vector.
    for tickets in string_sequence_vector[targetfile]:# for the tickets in string_sequence_vector with the targetfile is givien.
        string_sequence_vector[targetfile][tickets]= string_sequence_vector[targetfile][tickets] / computed_length[targetfile]
        #we decalre the string sqence value with the targetfile and the tickets where the string_sequence_vector and the targetfile tickets and divided with the cmputed length vwalue .
        if tickets not in computed_list_info:# if the given tickets are not in computed list info.
            computed_list_info[tickets]=Counter()# computed_list_info will count the tickets  in that list.
        computed_list_info[tickets][targetfile]=string_sequence_vector[targetfile][tickets]#we computed list info where the tickets
        # and the targets equals string sequence vactor and the targetfile and the tickets.



def query(qstring):                             #we define  the qstring function.
    qstring=qstring.lower()                     # qstring is converted into lower case to  have letter words .
    token_frequencies={}# considering   the token frequency no and  tuples.
    qlength=0#  we need to find the length of the q list.
    marker=0#markers of the list needed to be initializing as zero.
    temporary_string_value={}# we keep temporary_string_value as null tuple.
    string_dict={}## we take string dict
    cosine_similarity=Counter()                          # it will count the no  of similar  words in the cosine similarity
    for token in qstring.split():# for  the token in the qstring is splited.
        token=stemmer.stem(token)               # for the token  we equalises the stemmer.stem  from the token.
        if token not in computed_list_info:          #if the given token is not in the computed_list_info then we need to continue.
            continue
        if getidf(token)==0:                    #ifgetidf  of  token list and it compared with the 0.
            temporary_string_value[token], string_weight = zip(*computed_list_info[token].most_common())         #the temporary_string_value of token list ,string_weight should be equal to the zip
        else:# if the getidf(token) is =! 0
            temporary_string_value[token],string_weight = zip(*computed_list_info[token].most_common(10)) #we take the 10 values  from the list.
        string_dict[token]=string_weight[9] # we take the string_dictof token which will be equal to the 9 elements .
        if marker==1: ## if the marker is == 1.
            instersetion_strings=set(temporary_string_value[token]) & instersetion_strings  #if the instersetion_stringsn = set and the temporary_string_valueof token list and instersetion_strings.
        else:# if the marker is not equal to 1.
            instersetion_strings=set(temporary_string_value[token]) # the instersetion _ strings
            marker=1# if the marker =1.
        token_frequencies[token]=1+log10(qstring.count(token))    #token_frequencies of token list = one 10 times  the qstringtaken
        qlength+=token_frequencies[token]**2                      #the  value of the qlenght is calculated by the doubling  token_frequencies
    qlength=sqrt(qlength)# if the qlength is sqrt of q length
    for targetstring in string_sequence_vector:# for the  targetstring in the giving vector.
        temporary_similarity_value=0# we will make the temporary smimilarity value as zero.
        for token in token_frequencies:# for the token in the token frequencies.
            if targetstring in temporary_string_value[token]:# if tarettring in temporart value  is from the token list .
                temporary_similarity_value = temporary_similarity_value + (token_frequencies[token] / qlength) * computed_list_info[token][targetstring]       #then we add the similarity value ans token frequnecies(token) with the computed list info
            else:# if not the targetstring in the token list is not present then.
                temporary_similarity_value = temporary_similarity_value + (token_frequencies[token] / qlength) * string_dict[token]                    #then we add the similarity value and token frequencies of token with the computed list info.
        cosine_similarity[targetstring]=temporary_similarity_value # the cosine similarity  is equal to the temporary similariy value.
    local_max_value=cosine_similarity.most_common(1)     # the local_max_value will be   initializing to the coisne function.
    answer,weight=zip(*local_max_value)# we then weight the zip of the local max value with the answer.
    try:# we will add try to the program .
        if answer[0] in instersetion_strings: # if the answer of the 0 index is the  instersetion  with the string.
            return answer[0],weight[0]# retrun the answer with the zero index and the weight  with the 0 index.
        else:#  is no the index with the zero index then
            return "fetch more",0  # we will the return the  fetch more for the more elements.                                                          #i
    except UnboundLocalError:     # for the UnboundLocalError
        return "None",0# we will return the none 0 value

def getweight(targetfile,token):#  for the get wqeigh function we  take the target and token value
    return string_sequence_vector[targetfile][token]# we will then return the string_sequence_vector with th target and the token.


print("%.12f" % getidf("health"))#   the int vlaue is given where the keyword is the health

print("%.12f" % getidf("agenda"))# we take the agenda  keyword and  it is the int value .

print("%.12f" % getidf("vector"))# we take here the   keyword key vector and the getid if .


print("%.12f" % getidf("reason"))#   we take the keyword  reason where the count the getidf.


print("%.12f" % getidf("hispan"))#   we take the keyword  reason where the count the hispan where the hisan is  taken from the source  .
# 0.632023214705

print("%.12f" % getidf("hispanic"))# we take the hispanic  from the keyword to the getidf.
#-1.000000000000

print("%.12f" % getweight("2012-10-03.txt","health"))# from thesource code the health is taken from the getweight .
#0.008528366190

print("%.12f" % getweight("1960-10-21.txt","reason")) # from the reason  we get the getwweight from the reason
#0.000000000000

print("%.12f" % getweight("1976-10-22.txt","agenda"))# from the keyword   we take the agenda
#0.012683891289

print("%.12f" % getweight("2012-10-16.txt","hispan"))# we take hispan from the source code
#0.023489163449

print("%.12f" % getweight("2012-10-16.txt","hispanic"))# from  the source code the hispanic and the hispan is different .
#0.000000000000

print("(%s, %.12f)" % query("health insurance wall street")) #we take querey health insurace.
#(2012-10-03.txt, 0.033877975254)

print("(%s, %.12f)" % query("particular constitutional amendment")) #  we take %s for the character string.
#(fetch more, 0.000000000000)

print("(%s, %.12f)" % query("terror attack"))# from the list or data set  we have the terror keyowrd where the keyword is needed to gert the weight.
#(2004-09-30.txt, 0.026893338131)

print("(%s, %.12f)" % query("vector entropy"))# we all asked to get the weight of the vector entropy keyword where the keyowrd is enforced wi the the weight.
#(None, 0.000000000000)
