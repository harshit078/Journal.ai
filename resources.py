from links import *
import random


class Resource:
    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url


class Support:
    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url


def choose_resources(mood, ammount):
    # choose a random resource from the list of resources
    if mood == "anger":
        resources = anger_resources
    elif mood == "fear":
        resources = fear_resources
    elif mood == "joy":
        resources = joy_resources
    elif mood == "love":
        resources = love_resources
    elif mood == "sadness":
        resources = sadness_resources
    elif mood == "surprise":
        resources = surprise_resources

    nums = set()
    while len(nums) < 3:
        nums.add(random.randint(0, 4))

    return [
        Resource(resources[num][0], resources[num][1], resources[num][2])
        for num in nums
    ]


def choose_support(num):
    supports = (
     ("National Suicide Prevention Lifeline", 
     "The Lifeline provides 24/7, free and confidential support for people in distress, prevention and crisis resources for you or your loved ones, and best practices for professionals.",
     "https://suicidepreventionlifeline.org/"),
    ("Crisis Text Line", 
     "Text HOME to 741741 to connect with a crisis counselor. Free, 24/7 support.",
     "https://www.crisistextline.org/"),
    ("The Jed Foundation", 
     "Provides mental health resources, programs, and advocacy to empower teens and young adults.",
     "https://www.jedfoundation.org/"),
    ("The Trevor Project", 
     "Provides crisis intervention and suicide prevention services to LGBTQ youth.",
     "https://www.thetrevorproject.org/"),
    ("Depression and Bipolar Support Alliance (DBSA)", 
     "Offers support groups, online resources, and advocacy for people with depression and bipolar disorder.",
     "https://www.dbsalliance.org/"),
    ("Self-Help and Apps", 
     "There are many self-help resources and apps available to help manage depression symptoms. Here are a few resources to get you started:",
     "https://adaa.org/find-help/support/mental-health-apps"),
    )
    return Resource(supports[num][0], supports[num][1], supports[num][2])
