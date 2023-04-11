str = 'X-DSPAM-Confidence: 0.8475 '
findAfterColon = float(str[str.find(':') + 1 : ])
print(findAfterColon)