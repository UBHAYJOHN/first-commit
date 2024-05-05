def emoji_converter(message):
    # Define a dictionary mapping emoticons to emojis
    emoticon_to_emoji = {
        ":)": "😊",
        ":(": "😞",
        ";)": "😉",
        ":D": "😃",
        ":|": "😐",
    }
    
    # Replace emoticons with emojis
    for emoticon, emoji in emoticon_to_emoji.items():
        message = message.replace(emoticon, emoji)
    
    return message

# Example usage
message_with_emoticons = "I'm feeling :), but sometimes I feel :(. Do you know what I mean ;)?"
converted_message = emoji_converter(message_with_emoticons)
print(converted_message)
