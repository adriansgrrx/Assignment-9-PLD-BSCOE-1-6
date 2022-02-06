import json


myResume = {
  "basicDetails": [
    {
      "Name": "Adrian Remoquillo Esguerra",
      "Course/Year/Section": "BSCOE 1-6",
      "Age": "18 years old",
      "Address": "Taltal, Masinloc, Zambales",
      "Weight": "51 kg"
    }
  ],
  "contactDetails": [
    {
      "E-mail": "i.am.adrainsgrrx@gmail.com",
      "Cell-phone number": "0938-557-9510"
    }
  ],
  "education": [
    "Elementary Education: Taltal Elementary School",
    "Junior High School Education: Taltal National High School",
    "Senior High School: Northern Zambales College Inc.",
    "College: Currently studying at Polytechnic University of the Philippines(PUP)"
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
  ]
}

json_file = json.dumps(myResume, indent=2)
with open("myresume.json", "w") as resume: 
    resume.write(json_file)
