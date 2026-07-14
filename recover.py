def recover_text(garbled):
    try:
        # The garbled string is what happens when CP949 interprets UTF-8 bytes.
        # So encoding it back to CP949 gives us the original UTF-8 bytes!
        original_bytes = garbled.encode('cp949', errors='ignore')
        return original_bytes.decode('utf-8', errors='ignore')
    except Exception as e:
        return str(e)

garbled = "吏댴Ц?? 鍮쒖쎥씠 耳??삳떦"
print("Recovered:", recover_text(garbled))

# Read the file and try to recover it line by line
with open('c:/Users/user/workspace/stn-uiux/index/qrayon2.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

recovered_lines = []
for line in lines:
    recovered = recover_text(line)
    recovered_lines.append(recovered)

with open('c:/Users/user/workspace/stn-uiux/index/qrayon2_recovered.html', 'w', encoding='utf-8') as f:
    f.writelines(recovered_lines)
print("Saved recovered file")
