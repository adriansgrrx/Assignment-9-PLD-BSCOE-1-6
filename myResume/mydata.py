import json


myResume = {
  "basicDetails": [
    {
      "Full-Name": "Adrian Remoquillo Esguerra",
      "Sex": "Male",
      "Age": "18 years old",
      "Address": "Sherlock Holmes - 221B Baker St., London",
      "Height": "5'8 ft",
      "Weight": "50 kg"
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
    "Elem": "Hampden Gurney CofE Primary School",
    "JHS" : "North London Collegiate School",
    "SHS": "Godolphin & Latymer School",
    "Tert": "Imperial College London",
    }
  ],
  "achievements": [
    {
    "1": "Participant in Editorial Cartooning Division Level",
    "2": "Participant in Chess District Level",
    "3": "12th Place in Poster Making Contest Division Level",
    "4": "1st Place in Collaborative Desktop Publishing District Level",
    "5": "Participant in Collaborative Desktop Publishing Division Level",
    }
  ],
  "organizations": [
    {
    "yessci": "Yes-O Officer and Science Club Officer for 2 years straight",
    "ssg": "SSG Officer for 1 year"
    }
  ],
  "skills": [
    {
    "MS": "Microsoft Office Products",
    "Ps": "Photoshop",
    "DR": "Davinci Resolve",
    "TDraw": "Traditional and Digital Arts/Drawing",
    }
  ],
}

json_file = json.dumps(myResume, indent=2)
with open("myresume.json", "w") as resume: 
  resume.write(json_file)
