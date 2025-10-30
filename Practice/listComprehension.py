'''
chat  https://chatgpt.com/c/68594067-58fc-800f-84a5-ba31d9847493

'''
my_dict = {'Spider':'photographer','Bat':'philantropist','Wonder Wo': 'nurse'}

my_dict={key+'man':val for (key,val) in my_dict.items()} 
print(my_dict) 

## replace Spider with Superman !note the key!='Spider' refers to the new dicitionary my_dict={(key+'man' if key!='Spider' else 'Superman'): val for(key,val) in my_dict.items() } print(my_dict). if seems that the condition'if key != 'Spider' should be 'if key =='Spider'.
#1
my_dict = {'Spider': 'photographer', 'Bat': 'philantropist', 'Wonder Wo': 'nurse'}

my_dict = {
    (key + 'man' if key != 'Spider' else 'Superman'): val
    for (key, val) in my_dict.items()
}
## do key+man but this is False if key is Spider, then do Superman
## also look at it that do key+man if the key is not Spider, if is spider then do superman
print(my_dict)



my_dict = {'Spider':'photographer','Bat':'philantropist','Wonder Wo': 'nurse'}
# my_dict={key+'man':val for (key,val) in my_dict.items()}
# print(my_dict)
## replace Spider with Superman !note the key!='Spider' refers to the new dicitionary
my_dict1={(key+'man' if key!='Spider' else 'Superman'):
          (val if key!='Spider'else 'journalist') 
          for(key,val)  in my_dict.items()  }
print(my_dict1)


# my_dict={key +'man'if key !='Spider' else 'Superman' for(key,val) in my_dict.items()}

my_dict2={(key +'man'if key !='Spider' else 'Superman'):(val  if key != 'Spider' else 'newsman') for(key,val) in my_dict.items()}
print(my_dict2)
'''this says essentially: If the key is not 'Spider', then do key + 'man' (like 'Bat' becomes 'Batman')
But if the key is 'Spider', then make it 'Superman' instead.'''