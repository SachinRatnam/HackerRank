def designerPdfViewer(h, word):
    # Write your code here
    mx = 0
    for i in word:
        index = ord(i) - 97
        x = h[index]
        mx = max(mx,x)
    return mx * len(word)
