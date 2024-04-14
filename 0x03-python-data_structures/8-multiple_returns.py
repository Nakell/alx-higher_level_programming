#!/usr/bin/python3
def multiple_returns(sentence):
    sent_len = len(sentence)

    if sentence:
        first_letter = sentence[0]
    else:
        first_letter = None
    return (sent_len, first_letter)
