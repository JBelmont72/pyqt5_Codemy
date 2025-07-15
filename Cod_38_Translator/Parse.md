

# Parse data structure
dictionary of attributes returned by NSSpeechSynthesizer.attributesForVoice_() in macOS. This dictionary describes all metadata associated with a given voice, including:

language
voice ID
gender
name
supported characters
and more
Let’s parse and explain this data structure piece by piece:

✅ It is a Python Dictionary (dict)
Even though it looks like a macOS/Objective-C structure, Python (via PyObjC) wraps it as a native dict. You can treat it like any other dictionary.

You can inspect it like this:

for k, v in attrs.items():
    print(f"{k}: {v}")
🔍 Key Fields Explained
Key	Meaning
VoiceName	Human-readable name of the voice (e.g., "Zarvox")
VoiceIdentifier	Unique ID used to select the voice (e.g., "com.apple.speech.synthesis.voice.Zarvox")
VoiceLocaleIdentifier	BCP-47 locale code (e.g., "en_US", "he_IL", "fr_FR")
VoiceLanguage	Language code as string (e.g., "en-US")
VoiceGender	"VoiceGenderMale", "VoiceGenderFemale", or "VoiceGenderNeuter"
VoiceDemoText	Sample phrase said by this voice (e.g., "Hello! My name is Zarvox.")
VoiceNumericID	Internal numeric ID (not usually used)
VoiceGroup	Group tag (e.g., "VoiceGroupDefault")
VoiceNameRoot	Base name of the voice (often same as VoiceName)
🔤 Supported Characters
These two fields tell what characters the voice can speak:

VoiceSupportedCharacters: Unicode character ranges supported for normal text
VoiceIndividuallySpokenCharacters: Characters that may be spoken individually (e.g., for spelling)
Each item is a dictionary like:
{
  'UnicodeCharBegin': 33,
  'UnicodeCharEnd': 129
}

can be read as ranges:
chr(33) = '!'
chr(129) = <non-printable>

use in this form option:
for block in attrs['VoiceSupportedCharacters']:
    start = block['UnicodeCharBegin']
    end = block['UnicodeCharEnd']
    print(f"Supports Unicode {start}-{end} → {chr(start)} to {chr(end)}")
TO create a ;loanguage to voice mapping:   

from collections import defaultdict
lang_voice_map = defaultdict(list)

for voice_id in NSSpeechSynthesizer.availableVoices():
    attrs = NSSpeechSynthesizer.attributesForVoice_(voice_id)
    lang = attrs.get("VoiceLocaleIdentifier", "unknown")
    name = attrs.get("VoiceName", "Unnamed")
    lang_voice_map[lang].append((name, voice_id))

# Print voices per language
for lang, voices in lang_voice_map.items():
    print(f"\n{lang}:")
    for name, voice_id in voices:
        print(f"  - {name} → {voice_id}")
