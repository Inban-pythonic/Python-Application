def reverse(s):
    new_str=""
    for i in range(len(s)):
        new_str += s[len(s) -i -1]
    return(new_str)

print(reverse("123"))
print(reverse("adfgh"))




"""Hi Experts,
i have been trying to understand a code, it is a simple function to reverse a string, it surely can be done easily via other methods as well, but as of now i am trying to understand the used logic in below function.
if you can understand the function below, can you please help me in understanding it.

def reverse(s):
new_str= ""
for i in range(len(s)):
new_str += s[len(s) -i - 1]
return(new_str)

print(reverse("123"))
print(reverse("adfgh"))

Thanks for your time and kindness :)
if you have other method of doing it , please feel """
