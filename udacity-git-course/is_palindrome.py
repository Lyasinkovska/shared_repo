def alpha(text):
    text_alpha = ""
    for i in text:
        if i.isalpha():
            text_alpha = "".join([text_alpha, i])
    return text_alpha.lower()

def reverse(text):
    return alpha(text[::-1].lower())

def is_palindrome(text):
    if alpha(text) == reverse(text):
        return "Yes, it is a palindrome"
    else:
        return "No, it is not a palindrome"



print(reverse("Rise to vote, sir."))

print(is_palindrome("Rise to vote, sir." ))
