# LearningGenerator

## Description:

Custom learning path where, given a prompt such as "I want to learn data science in 12 weeks", identifies what needs to
be learned and generates subtopics including videos and quizzes and builds a plan to learn the topic on the fly.
Tailors the learning to the specific user. Can upgrade the pace and skip irrelevant sections.

## Problem:

It is hard to find a good course or series to learn niche or custom topics at a self-paced environment.

## MVP:

1) User input which takes and processes the input for the requirements of the course including content, time
   constraints, preferences, etc. to identify a list of modules and the order to complete them.
2) Output a section-by-section (essentially week-by-week) course with

* summaries: summary of module
* videos: custom video explanations
* quizzes: custom quizzes after each video to test learning. Eventually: if the user does bad on the quiz, generate more
  content to teach the user.
* resources: Articles and sources for further reading
* test: a test at the end of the section covering all of the content in increasing difficulty. When the user starts
  getting questions wrong, test ends.

Need:
**Create module**

```json
{
  "id" : "uuid" ,
  "name" : "Retrieval-Augmented Generation" ,
  "description" : "" ,
  "summary" : "" ,
  // scale of (easiest) 1-3 (hardest)
  "difficulty" : 3 ,
  "prerequisites" : [
    "intro to ai" ,
    "python for beginners"
  ] ,
  // manually decided
  "quality" : 0.85
  // minutes
  "duration" : 25
  "created_at" : "2025-09-03T15:32:48Z" ,
  "videos" : [
    {
      "id" : "id" ,
      "title" : "Module Introduction" ,
      "summary" : "" ,
      "script" : "" ,
      "url" : "https://..." ,
      "duration" : "" ,
      "views" : 100
    }
  ] ,
  "resources" : [
    {
      "title" : "name" ,
      "url" : "url" ,
      "description" : "description" ,
      "summary" : "summary"
    }
  ] ,
  "quizzes" : [
    {
      "title" : "" ,
      "quiz" : [
        {
          "question" : "What is 6 + 1?" ,
          "difficulty" : 0.7 ,
          "options" : [
            {
              "value" : "45" ,
              "correct" : false ,
              "explanation" : "This is wrong because..."
            } ,
            {
              "value" : "7" ,
              "correct" : True ,
              "explanation" : "Correct! When you add it, this is the value."
            }
          ]
        }
      ]
    }
  ] ,
  "test" : [{
    ... // same as quiz but more questions
  }]
}
```