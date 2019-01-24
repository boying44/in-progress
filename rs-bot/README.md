- [ ] Detect health
    - [X] Detech health bar
    - [ ] Recognize health digit
- [X] Eat Food
    - [ ] Check if transparant background affects finding Salmon
- [x] Detect monster
    - [ ] Choose untaken giant
- [ ] Pick up item
- [ ] Screenshot choose window

Run with Python3


Thought process:
Giant detection
    - Object detection?
        Problem: would have to train machine learning model to identify the giant
    - Solution:
        - Use a color mask to filter giant's location
        - Find the contours in the mask - a giant end up as several big and small contours
        - Use center of big contours to get an approximate giant location
Health detection
    - OCR on health status doesn't work
    - Percentage based health bar seems too hard
        - How to get health bar vs other people's
        - Center health bar might work