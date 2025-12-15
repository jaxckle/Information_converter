import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load cleaned CSV with integer labels
df = pd.read_csv('numeric_format_training_int_pandas.csv')

# Map the 'value' column (strings) to numeric features
# Example: convert each character to ASCII codes and pad to length 8
def easy_features(s):
    s = str(s).upper()
    is_bin = all(c in '01' for c in s)
    is_dec = all(c in '0123456789' for c in s)
    is_hex = all(c in '0123456789ABCDEF' for c in s)
    return [len(s), int(is_bin), int(is_dec), int(is_hex)]

X = df['value'].apply(easy_features).tolist()
y = df['label'].tolist()

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=17, train_size=0.8)

# Train Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=17)
rf.fit(X_train, y_train)

# Predict
y_pred = rf.predict(X_test)

# Evaluate
accuracy = rf.score(X_test, y_test)

num_hex={
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F"
}

# the conversion of lists 
def reverse_list(num_list):
    reversed=[]
    for i in range(len(num_list)-1, -1, -1):
        reversed.append(num_list[i])
    return reversed
def num_to_hex(num_list):
    for i in range(0,len(num_list)):
        if num_list[i] in num_hex:
            num_list[i]=num_hex.get(num_list[i])
    return num_list
def letter_convert(hex_list):
    new = []
    for c in hex_list:
        if c.isdigit():
            new.append(int(c))
        else:
            for k, v in num_hex.items():
                if v == c.upper():
                    new.append(k)
                    break
    return new
# the coverting functions
def dec_hex(num):
    hex_list=[]
    while num>=1:
        remainder_calc = num%16
        hex_list.append(remainder_calc)
        num = int(num/16)
    return reverse_list(num_to_hex(hex_list))
def dec_bi(num):
    binary_list = []
    while num > 0:
        bit = num % 2  
        binary_list.append(bit)
        num //= 2         
    binary_list.reverse()   
    return binary_list
def hex_dec(hex_list):
    hex_list=letter_convert(hex_list)
    x=len(hex_list)-1
    for i in range(0,len(hex_list)):
        convert=hex_list[i]
        convert=16**x*convert
        hex_list[i]=convert
        x=x-1
    return sum(hex_list)
def hex_bi(hex_list):
    byte_list = []
    full_list = []
    hex_list = letter_convert(hex_list)
    for i in range(len(hex_list)):
        value = hex_list[i] 
        for _ in range(4): 
            bit = value % 2  
            byte_list.append(bit)
            value //= 2  
        byte_list.reverse()     
        full_list.append(byte_list.copy())  
        byte_list.clear()     
    return full_list
def bi_dec(bi_list):
    num = 0
    x=0
    for i in reverse_list(bi_list):
        if i==1:
            num+=2**x
        x+=1
    return num 
def bi_hex(bi_list):
    return dec_hex(bi_dec(bi_list))
# full convertion
def full_dec(num):
    return dec_hex(num),dec_bi(num)
def full_hex(hex_list):
    return hex_dec(hex_list),hex_bi(hex_list)
def full_bi(bi_list):
    return bi_dec(bi_list),bi_hex(bi_list)


user_input=input("Enter the number you want to convert: ")

AI_understand = [easy_features(user_input)]

predicted_format = rf.predict(AI_understand)[0]

label_map_reverse = {
    0: 'Binary',
    1: 'Decimal',
    2: 'Hexadecimal',
    3: 'Unknown'
}

predicted_format_name = label_map_reverse[predicted_format]

print(f"The predicted format is: {predicted_format_name}")

if predicted_format_name=="Decimal":
    print(full_dec(int(user_input)))
elif predicted_format_name=="Hexadecimal":
    hex_list=list(user_input)
    print(full_hex(hex_list))
elif predicted_format_name=="Binary":
    bi_list=[int(bit) for bit in user_input]
    print(full_bi(bi_list))
elif predicted_format_name=="Unknown":
    print("The format could not be determined.")        