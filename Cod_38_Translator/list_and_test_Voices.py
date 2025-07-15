'''first is the program to list and select language to be spoken
second file after some notes is my attempt to parse the data structure

/Users/judsonbelmont/Documents/Shared_Folders/pyqt5_Codemy/Cod_38_Translator/list_and_test_Voices.py
Here’s a macOS-only Python script that:

Lists available voices grouped by language.
Lets you test a voice by typing text.
Helps you build a dictionary of preferred voices (e.g. for your language_to_voice mapping).

'''
# from AppKit import NSSpeechSynthesizer
# from collections import defaultdict

# # Get available voices and their attributes
# voices = NSSpeechSynthesizer.availableVoices()
# print('type for voices: ',type(voices))
# lang_voice_map = defaultdict(list)

# print("🔍 Gathering available voices...\n")

# for voice in voices:
#     print('voice is : ',voice)
#     attrs = NSSpeechSynthesizer.attributesForVoice_(voice)
#     lang = attrs.get("VoiceLocaleIdentifier", "Unknown")
#     name = attrs.get("VoiceName", "Unnamed")
#     lang_voice_map[lang].append((name, voice))
#     print('my attrs:: ',attrs)
    
# # Print grouped voices
# for lang, voice_list in sorted(lang_voice_map.items()):
#     print(f"\n🌐 Language: {lang}")
#     for i, (name, voice_id) in enumerate(voice_list):
#         print(f"  [{i}] {name:<20} - {voice_id}")

# # Prompt to test a voice
# while True:
#     lang_input = input("\nEnter language code to test a voice (e.g. 'es_ES', 'he_IL', 'fr_FR', or 'q' to quit): ").strip()
#     if lang_input.lower() == 'q':
#         break
#     if lang_input not in lang_voice_map:
#         print("❌ Language not found. Try again.")
#         continue

#     voice_options = lang_voice_map[lang_input]
#     for i, (name, _) in enumerate(voice_options):
#         print(f"[{i}] {name}")

#     index_input = input("Select voice index to test: ").strip()
#     if not index_input.isdigit() or int(index_input) >= len(voice_options):
#         print("❌ Invalid index. Try again.")
#         continue

#     _, voice_id = voice_options[int(index_input)]

#     test_text = input("Type a sentence to speak: ").strip()
#     if test_text:
#         speaker = NSSpeechSynthesizer.alloc().init()
#         speaker.setVoice_(voice_id)
#         speaker.startSpeakingString_(test_text)
#         print(f"✅ Speaking with {voice_id}...\n")

# print("👋 Done.")


# ✅ 1. List All Available Voices (and their locales)
# Run this Python snippet to print the available voices on your system:

# from AppKit import NSSpeechSynthesizer

# for voice in NSSpeechSynthesizer.availableVoices():
#     print(voice)


#  this will print voice identifiers like:
# com.apple.ttsbundle.Monica-compact
# com.apple.ttsbundle.Thomas-compact
# com.apple.speech.synthesis.voice.Yuri
# com.apple.speech.synthesis.voice.Karen

# ✅ 2. Get Voice Attributes (language, name, etc.)
# To see which voice speaks which language, run:
    
# from AppKit import NSSpeechSynthesizer, NSSpeechSynthesizerAttributes

# for voice in NSSpeechSynthesizer.availableVoices():
#     desc = NSSpeechSynthesizer.attributesForVoice_(voice)
#     print(f"{voice} -> {desc.get('VoiceLocaleIdentifier', '')} | {desc.get('VoiceName', '')}")

# output will look like this:
#     com.apple.ttsbundle.Monica-compact -> es_ES | Monica
# com.apple.ttsbundle.Thomas-compact -> fr_FR | Thomas
# com.apple.speech.synthesis.voice.Carmit -> he_IL | Carmit
# com.apple.speech.synthesis.voice.Damayanti -> hi_IN | Damayanti

# ✅ 3. Add Hebrew and Latin (if available)
# 🕎 Hebrew  "hebrew": "com.apple.speech.synthesis.voice.Carmit"




# Most macOS installs come with:

# "hebrew": "com.apple.speech.synthesis.voice.Carmit"
# 🏛️ Latin      "latin": "com.apple.speech.synthesis.voice.Luca"  # Italian


# macOS does not include Latin as a TTS language out of the box, but you could simulate Latin pronunciation using an Italian or English voice, e.g.:

# "latin": "com.apple.speech.synthesis.voice.Luca"  # Italian
# Or manually select a voice that reads it well enough.

# ✅ 4. Update Your language_to_voice Dictionary
# Here’s how to expand your dictionary:
# self.language_to_voice = {
#     "spanish": "com.apple.ttsbundle.Monica-compact",
#     "german": "com.apple.ttsbundle.Anna-compact",
#     "french": "com.apple.ttsbundle.Thomas-compact",
#     "hebrew": "com.apple.speech.synthesis.voice.Carmit",
#     "latin": "com.apple.speech.synthesis.voice.Luca",  # Fallback to Italian
# }

# ✅ 5. (Optional) Install Additional Voices on macOS
# Go to System Settings > Accessibility > Spoken Content > System Voice > Manage Voices…

# You can download voices for:

# Arabic, Greek, Korean, Hebrew, Hindi
# Many regional English variants
# …but not Latin




# voice is :  com.apple.speech.synthesis.voice.Zarvox
# my attrs::  {
#     VoiceDemoText = "Hello! My name is Zarvox.";
#     VoiceGender = VoiceGenderNeuter;
#     VoiceGroup = VoiceGroupDefault;
#     VoiceIdentifier = "com.apple.speech.synthesis.voice.Zarvox";
#     VoiceIndividuallySpokenCharacters =     (
#                 {
#             UnicodeCharBegin = 33;
#             UnicodeCharEnd = 129;
#         },
#                 {
#             UnicodeCharBegin = 141;
#             UnicodeCharEnd = 141;
#         },
#                 {
#             UnicodeCharBegin = 143;
#             UnicodeCharEnd = 144;
#         },
#                 {
#             UnicodeCharBegin = 157;
#             UnicodeCharEnd = 157;
#         },
#                 {
#             UnicodeCharBegin = 160;
#             UnicodeCharEnd = 255;
#         },
#                 {
#             UnicodeCharBegin = 338;
#             UnicodeCharEnd = 339;
#         },
#                 {
#             UnicodeCharBegin = 352;
#             UnicodeCharEnd = 353;
#         },
#                 {
#             UnicodeCharBegin = 376;
#             UnicodeCharEnd = 376;
#         },
#                 {
#             UnicodeCharBegin = 381;
#             UnicodeCharEnd = 382;
#         },
#                 {
#             UnicodeCharBegin = 402;
#             UnicodeCharEnd = 402;
#         },
#                 {
#             UnicodeCharBegin = 710;
#             UnicodeCharEnd = 710;
#         },
#                 {
#             UnicodeCharBegin = 732;
#             UnicodeCharEnd = 732;
#         },
#                 {
#             UnicodeCharBegin = 8211;
#             UnicodeCharEnd = 8212;
#         },
#                 {
#             UnicodeCharBegin = 8216;
#             UnicodeCharEnd = 8218;
#         },
#                 {
#             UnicodeCharBegin = 8220;
#             UnicodeCharEnd = 8222;
#         },
#                 {
#             UnicodeCharBegin = 8224;
#             UnicodeCharEnd = 8226;
#         },
#                 {
#             UnicodeCharBegin = 8230;
#             UnicodeCharEnd = 8230;
#         },
#                 {
#             UnicodeCharBegin = 8240;
#             UnicodeCharEnd = 8240;
#         },
#                 {
#             UnicodeCharBegin = 8249;
#             UnicodeCharEnd = 8250;
#         },
#                 {
#             UnicodeCharBegin = 8352;
#             UnicodeCharEnd = 8352;
#         },
#                 {
#             UnicodeCharBegin = 8364;
#             UnicodeCharEnd = 8364;
#         },
#                 {
#             UnicodeCharBegin = 8482;
#             UnicodeCharEnd = 8482;
#         }
#     );
#     VoiceLanguage = "en-US";
#     VoiceLocaleIdentifier = "en_US";
#     VoiceName = Zarvox;
#     VoiceNameRoot = Zarvox;
#     VoiceNumericID = 1483995744;
#     VoiceSupportedCharacters =     (
#                 {
#             UnicodeCharBegin = 33;
#             UnicodeCharEnd = 129;
#         },
#                 {
#             UnicodeCharBegin = 141;
#             UnicodeCharEnd = 141;
#         },
#                 {
#             UnicodeCharBegin = 143;
#             UnicodeCharEnd = 144;
#         },
#                 {
#             UnicodeCharBegin = 157;
#             UnicodeCharEnd = 157;
#         },
#                 {
#             UnicodeCharBegin = 160;
#             UnicodeCharEnd = 255;
#         },
#                 {
#             UnicodeCharBegin = 338;
#             UnicodeCharEnd = 339;
#         },
#                 {
#             UnicodeCharBegin = 352;
#             UnicodeCharEnd = 353;
#         },
#                 {
#             UnicodeCharBegin = 376;
#             UnicodeCharEnd = 376;
#         },
#                 {
#             UnicodeCharBegin = 381;
#             UnicodeCharEnd = 382;
#         },
#                 {
#             UnicodeCharBegin = 402;
#             UnicodeCharEnd = 402;
#         },
#                 {
#             UnicodeCharBegin = 710;
#             UnicodeCharEnd = 710;
#         },
#                 {
#             UnicodeCharBegin = 732;
#             UnicodeCharEnd = 732;
#         },
#                 {
#             UnicodeCharBegin = 8211;
#             UnicodeCharEnd = 8212;
#         },
#                 {
#             UnicodeCharBegin = 8216;
#             UnicodeCharEnd = 8218;
#         },
#                 {
#             UnicodeCharBegin = 8220;
#             UnicodeCharEnd = 8222;
#         },
#                 {
#             UnicodeCharBegin = 8224;
#             UnicodeCharEnd = 8226;
#         },
#                 {
#             UnicodeCharBegin = 8230;
#             UnicodeCharEnd = 8230;
#         },
#                 {
#             UnicodeCharBegin = 8240;
#             UnicodeCharEnd = 8240;
#         },
#                 {
#             UnicodeCharBegin = 8249;
#             UnicodeCharEnd = 8250;
#         },
#                 {
#             UnicodeCharBegin = 8352;
#             UnicodeCharEnd = 8352;
#         },
#                 {
#             UnicodeCharBegin = 8364;
#             UnicodeCharEnd = 8364;
#         },
#                 {
#             UnicodeCharBegin = 8482;
#             UnicodeCharEnd = 8482;
#         }
#     );
# }


# from AppKit import NSSpeechSynthesizer
# from collections import defaultdict

# # Get available voices and their attributes
# voices = NSSpeechSynthesizer.availableVoices()
# print('type for voices: ',type(voices))
# lang_voice_map = defaultdict(list)

# print("🔍 Gathering available voices...\n")

# for voice in voices:
#     print('voice is : ',voice[0])
#     attrs = NSSpeechSynthesizer.attributesForVoice_(voice[0])
#     lang = attrs.get("VoiceLocaleIdentifier", "Unknown")
#     name = attrs.get("VoiceName", "Unnamed")
#     lang_voice_map[lang].append((name, voice[0]))
    
#     # print('my attrs:: ',attrs)
    
# # Print grouped voices
# for lang, voice_list in sorted(lang_voice_map.items()):
#     print(f"\n🌐 Language: {lang}")
#     for i, (name, voice_id) in enumerate(voice_list):
#         print(f"  [{i}] {name:<20} - {voice_id}")

#####
import platform
from AppKit import NSSpeechSynthesizer

# Get list of available voice identifiers
voices = NSSpeechSynthesizer.availableVoices()
print(type(voices)) # output: <objective-c class __NSArrayI at 0x2071acff0>
print(voices[:3]) ## output: a list  of three voices( "com.apple.speech.synthesis.voice.Albert", "com.apple.voice.compact.it-IT.Alice",....)
print(type(voices[0]))  #<class 'objc.pyobjc_unicode'>
print(voices[0])        #com.apple.speech.synthesis.voice.Albert


print(f"\n➡️ Level 0: voices (type: {type(voices)})")
print(f"Total voices: {len(voices)}")
print(f"voices[0]: {voices[0]}")  # This is a string

# Drill into the first voice
voice_id = voices[0]
print(f"\n➡️ Level 1: voice_id = voices[0]")
print(f"voice_id: {voice_id} (type: {type(voice_id)})")

# Get the attributes dictionary for that voice
# attrs = NSSpeechSynthesizer.attributesForVoice_(voice_id)
attrs = NSSpeechSynthesizer.attributesForVoice_(voices[0])
# print(f"\n➡️ Level 2: attributes = NSSpeechSynthesizer.attributesForVoice_({voice_id})")
print(f"\n➡️ Level 2: attributes = NSSpeechSynthesizer.attributesForVoice_({voices[0]})")
print(f"type: {type(attrs)}")   #output:  type: <objective-c class __NSDictionaryM at 0x2071ad400>

# Drill into the top-level keys in the attribute dictionary
print("\n➡️ Level 3: keys and values in attributes (one by one)")
for key, value in attrs.items():
    print(f"Key: {key} | Type: {type(value)}")
    if isinstance(value, (str, int)):
        print(f'Key: {key}')
        print(f"  Value: {value}")
    elif isinstance(value, list):
        print(f"  Value is a list of {len(value)} items")
        print("  -> Showing first item:")

        # Drill into first item of the list
        first_item = value[0]
        print(f"    First item type: {type(first_item)}")

        # If it's a dictionary inside the list, print its keys
        if isinstance(first_item, dict):
            for k, v in first_item.items():
                print(f"      {k} : {v}")
        else:
            print(f"    Value: {first_item}")

    elif isinstance(value, dict):
        print("  Nested dictionary:")
        for k, v in value.items():
            print(f"    {k} : {v}")
    else:
        print(f"  Unhandled type: {type(value)}")

# Optional: print the demo text for clarity
print(f"\n➡️ Sample demo text:\n{attrs.get('VoiceDemoText')} and Judson just worked his way down to me!")

## make into a class where I can enter the voice indeex
import platform
from AppKit import NSSpeechSynthesizer






# Get list of available voice identifiers
voices = NSSpeechSynthesizer.availableVoices()
print(type(voices)) # output: <objective-c class __NSArrayI at 0x2071acff0>
print(voices[:3]) ## output: a list  of three voices( "com.apple.speech.synthesis.voice.Albert", "com.apple.voice.compact.it-IT.Alice",....)
print(type(voices[0]))  #<class 'objc.pyobjc_unicode'>
print(voices[0])        #com.apple.speech.synthesis.voice.Albert


print(f"\n➡️ Level 0: voices (type: {type(voices)})")
print(f"Total voices: {len(voices)}")
print(f"voices[0]: {voices[0]}")  # This is a string

# Drill into the first voice
voice_id = voices[0]
print(f"\n➡️ Level 1: voice_id = voices[0]")
print(f"voice_id: {voice_id} (type: {type(voice_id)})")

# Get the attributes dictionary for that voice
# attrs = NSSpeechSynthesizer.attributesForVoice_(voice_id)
attrs = NSSpeechSynthesizer.attributesForVoice_(voices[0])
# print(f"\n➡️ Level 2: attributes = NSSpeechSynthesizer.attributesForVoice_({voice_id})")
print(f"\n➡️ Level 2: attributes = NSSpeechSynthesizer.attributesForVoice_({voices[0]})")
print(f"type: {type(attrs)}")   #output:  type: <objective-c class __NSDictionaryM at 0x2071ad400>

# Drill into the top-level keys in the attribute dictionary
print("\n➡️ Level 3: keys and values in attributes (one by one)")
for key, value in attrs.items():
    print(f"Key: {key} | Type: {type(value)}")
    if isinstance(value, (str, int)):
        print(f'Key: {key}')
        print(f"  Value: {value}")
    elif isinstance(value, list):
        print(f"  Value is a list of {len(value)} items")
        print("  -> Showing first item:")

        # Drill into first item of the list
        first_item = value[0]
        print(f"    First item type: {type(first_item)}")

        # If it's a dictionary inside the list, print its keys
        if isinstance(first_item, dict):
            for k, v in first_item.items():
                print(f"      {k} : {v}")
        else:
            print(f"    Value: {first_item}")

    elif isinstance(value, dict):
        print("  Nested dictionary:")
        for k, v in value.items():
            print(f"    {k} : {v}")
    else:
        print(f"  Unhandled type: {type(value)}")

# Optional: print the demo text for clarity
print(f"\n➡️ Sample demo text:\n{attrs.get('VoiceDemoText')} and Judson just worked his way down to me!")