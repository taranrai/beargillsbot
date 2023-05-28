import re

def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    parsed_data = []
    conversation_pair = []
    current_sender = None

    for line in lines:
        line = line.strip()

        # The regular expression pattern for the date, time, and sender
        pattern = r'^\[\d{2}/\d{2}/\d{4},\s\d{2}:\d{2}:\d{2}\]\s([^:]*):'
        match = re.search(pattern, line)

        # If the pattern matches, this line is the start of a new message
        if match:
            sender = match.group(1)
            message = line[len(match.group(0)):].strip()

            if current_sender is None:
                # This is the first message in the conversation
                conversation_pair.append(message)
            elif sender == current_sender:
                # This message is from the same sender as the previous message
                conversation_pair[-1] += ' ' + message
            else:
                # This message is from a different sender
                conversation_pair.append(message)
                if len(conversation_pair) == 2:
                    parsed_data.append(tuple(conversation_pair))
                    conversation_pair = [conversation_pair[-1]]

            current_sender = sender

    return parsed_data


file_path = 'xxxxxxxxxxxxxxxxxxx'  # Replace with your file path
conversations = parse_file(file_path)

# Now 'conversations' is a list of tuples in the format (message, response)
for conversation in conversations:
    print(conversation)



