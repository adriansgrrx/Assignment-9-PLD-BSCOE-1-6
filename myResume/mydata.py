import json


myResume = {
  "basicDetails": [
    {
      "Full-Name": "Adrian Remoquillo Esguerra",
      "Age": "24 years old",
      "Address": "Sherlock Holmes - 221B Baker St., London",
      "Weight": "55 kg"
    }
  ],
  "contactDetails": [
    {
      "E-mail": "peterparker08@gmail.com",
      "Cell-phone number": "0929-123-4567"
    }
  ],
  "education": [
    {
    "Elem": "Taltal Elementary School",
    "JHS" : "Taltal National High School",
    "SHS": "Northern Zambales College Inc.",
    "Tert": "Polytechnic University of the Philippines(PUP)",
    "Course": "Bachelor of Science in Computer Engineering",
    }
  ],
  "achievementsJHS": [
    "With Honors",
    "Participant in Editorial Cartooning Division Level",
    "2nd Place in Collaborative Desktop Publishing District Level",
    "Participant in Chess District Level12th Place in Poster Making Contest Division Level"
  ],
  "achievementsSHS": [
    "With High Honors",
    "1st Place in Collaborative Desktop Publishing District Level",
    "Participant in Collaborative Desktop Publishing Division Level",
    "Supreme Student Government Officer"
  ],
  "reference": [
    "John Florentino E. Echon EdD",
    "Teacher III",
    "Taltal National High School",
    "0977-025-7009",
    "johnflorentino.echon@deped.gov.ph"
  ],
  "skills": [
    "Photoshop",
    "Davinci Resolve",
    "Traditional Arts/Drawing",
    "Digital Arts/Drawing"
  ],
}

json_file = json.dumps(myResume, indent=2)
with open("myresume.json", "w") as resume: 
    resume.write(json_file)
