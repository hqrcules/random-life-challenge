from django.core.management.base import BaseCommand
from challenges.models import Category, Challenge


class Command(BaseCommand):
    help = 'Seeds the database with initial categories and challenges'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        Category.objects.all().delete()
        Challenge.objects.all().delete()

        self.stdout.write('Creating new data...')

        physical, _ = Category.objects.get_or_create(name='Physical')
        intellectual, _ = Category.objects.get_or_create(name='Intellectual')
        creative, _ = Category.objects.get_or_create(name='Creative')
        social, _ = Category.objects.get_or_create(name='Social')
        mindfulness, _ = Category.objects.get_or_create(name='Mindfulness')

        challenges = [
            # === Physical Challenges ===
            # These challenges focus on improving your physical health and fitness through various activities.
            {'category': physical, 'title': '30-Minute Walk', 'description': 'Go for a brisk 30-minute walk outside.'},
            {'category': physical, 'title': '10-Minute Stretching', 'description': 'Do a full-body stretching routine for 10 minutes.'},
            {'category': physical, 'title': '20 Push-ups', 'description': 'Complete 20 push-ups, in sets if necessary.'},
            {'category': physical, 'title': 'Drink 8 Glasses of Water', 'description': 'Ensure you drink at least 8 glasses of water throughout the day.'},
            {'category': physical, 'title': '30 Squats', 'description': 'Perform 30 bodyweight squats with proper form.'},
            {'category': physical, 'title': '15-Minute Jog', 'description': 'Go for a light jog in a park or around your neighborhood.'},
            {'category': physical, 'title': 'Plank for 60 Seconds', 'description': 'Hold a plank position for a total of 60 seconds.'},
            {'category': physical, 'title': 'Take the Stairs', 'description': 'Whenever possible, take the stairs instead of the elevator for the entire day.'},
            {'category': physical, 'title': 'Do 15 Lunges', 'description': 'Perform 15 lunges per leg (30 total).'},
            {'category': physical, 'title': '10-Minute Yoga Flow', 'description': 'Follow a simple 10-minute yoga flow online (e.g., Sun Salutation).'},
            {'category': physical, 'title': 'Climb 5 Flights of Stairs', 'description': 'Find a staircase and climb up and down 5 flights.'},
            {'category': physical, 'title': '5-Minute Core Workout', 'description': 'Do a 5-minute core workout (planks, crunches, leg raises).'},
            {'category': physical, 'title': 'Jump Rope for 5 Minutes', 'description': 'Jump rope continuously for 5 minutes.'},
            {'category': physical, 'title': 'Wall Sit for 60 Seconds', 'description': 'Hold a wall sit position for 60 seconds.'},
            {'category': physical, 'title': '15 Burpees', 'description': 'Complete 15 burpees with proper form.'},
            {'category': physical, 'title': 'Mountain Climbers for 2 Minutes', 'description': 'Do mountain climbers for 2 minutes straight.'},
            {'category': physical, 'title': 'Balance on One Foot', 'description': 'Stand on one foot for 30 seconds, then switch.'},
            {'category': physical, 'title': 'Arm Circles', 'description': 'Do 30 forward arm circles and 30 backward arm circles.'},
            {'category': physical, 'title': 'Calf Raises', 'description': 'Perform 3 sets of 15 calf raises.'},
            {'category': physical, 'title': 'Deep Breathing Exercise', 'description': 'Take 5 deep breaths, holding each for 10 seconds.'},

            # === Intellectual Challenges ===
            # These challenges are designed to stimulate your mind, expand your knowledge, and improve cognitive abilities.
            {'category': intellectual, 'title': 'Read a Book for 20 Minutes', 'description': 'Read a chapter of a book or read for 20 minutes straight.'},
            {'category': intellectual, 'title': 'Solve a Sudoku Puzzle', 'description': 'Find and solve a Sudoku puzzle of any difficulty.'},
            {'category': intellectual, 'title': 'Learn 5 New Words', 'description': 'Learn five new words in a foreign language or your native one.'},
            {'category': intellectual, 'title': 'Watch a Documentary', 'description': 'Watch an educational documentary on a topic you know little about.'},
            {'category': intellectual, 'title': 'Plan Your Week', 'description': 'Spend 15 minutes planning your goals and tasks for the upcoming week.'},
            {'category': intellectual, 'title': 'Listen to a Podcast', 'description': 'Listen to an episode of an educational or thought-provoking podcast.'},
            {'category': intellectual, 'title': 'Research a New Topic', 'description': 'Spend 20 minutes learning about something completely new to you online.'},
            {'category': intellectual, 'title': 'Write a Book Summary', 'description': 'Write a short summary (100-150 words) of a book you recently read.'},
            {'category': intellectual, 'title': 'Play a Strategy Game', 'description': 'Play a strategy game like chess, checkers, or a puzzle game for 15 minutes.'},
            {'category': intellectual, 'title': 'Take an Online Quiz', 'description': 'Find an online quiz on a subject you are curious about and complete it.'},
            {'category': intellectual, 'title': 'Learn a Historical Fact', 'description': 'Research and write down one interesting historical fact you didn\'t know before.'},
            {'category': intellectual, 'title': 'Write a Short Story', 'description': 'Write a 200-word short story on any topic.'},
            {'category': intellectual, 'title': 'Solve a Crossword Puzzle', 'description': 'Complete a crossword puzzle from a newspaper or online.'},
            {'category': intellectual, 'title': 'Learn Basic Sign Language', 'description': 'Learn 5 basic sign language gestures.'},
            {'category': intellectual, 'title': 'Create a Mind Map', 'description': 'Create a mind map of a topic you\'re passionate about.'},
            {'category': intellectual, 'title': 'Memorize a Poem', 'description': 'Memorize a short poem (10-15 lines).'},
            {'category': intellectual, 'title': 'Learn Roman Numerals', 'description': 'Learn to count from 1 to 20 in Roman numerals.'},
            {'category': intellectual, 'title': 'Identify Cloud Types', 'description': 'Learn to identify 3 different types of clouds.'},
            {'category': intellectual, 'title': 'Practice Mental Math', 'description': 'Solve 10 basic math problems without a calculator.'},
            {'category': intellectual, 'title': 'Learn Morse Code', 'description': 'Learn the Morse code for your name.'},

            # === Creative Challenges ===
            # These challenges encourage artistic expression, innovation, and exploration of creative outlets.
            {'category': creative, 'title': 'Sketch for 15 Minutes', 'description': 'Draw or sketch anything that comes to mind for 15 minutes.'},
            {'category': creative, 'title': 'Write a Short Poem', 'description': 'Write a poem about your day or current mood.'},
            {'category': creative, 'title': 'Cook a New Recipe', 'description': 'Try cooking a simple recipe you have never made before.'},
            {'category': creative, 'title': 'Listen to a New Music Genre', 'description': 'Explore a music genre you are unfamiliar with for 20 minutes.'},
            {'category': creative, 'title': 'Take a Photo', 'description': 'Take a picture of something you find beautiful or interesting today.'},
            {'category': creative, 'title': 'Write a Journal Entry', 'description': 'Write about your thoughts and feelings for 10 minutes.'},
            {'category': creative, 'title': 'Organize a Room', 'description': 'Spend 20 minutes decluttering or organizing a small area of your home.'},
            {'category': creative, 'title': 'Create a Playlist', 'description': 'Make a playlist of 10 songs for a specific mood or activity.'},
            {'category': creative, 'title': 'DIY Craft Project', 'description': 'Do a small DIY craft project using materials you already have at home.'},
            {'category': creative, 'title': 'Redecorate a Corner', 'description': 'Rearrange or redecorate a small corner of your room to refresh the space.'},
            {'category': creative, 'title': 'Write a Letter', 'description': 'Write a handwritten letter to a friend or family member.'},
            {'category': creative, 'title': 'Design a Logo', 'description': 'Create a simple logo for yourself or a fictional company.'},
            {'category': creative, 'title': 'Make a Collage', 'description': 'Create a collage using old magazines or printed images.'},
            {'category': creative, 'title': 'Write a Haiku', 'description': 'Write a traditional Japanese haiku (5-7-5 syllables).'},
            {'category': creative, 'title': 'Create a Vision Board', 'description': 'Make a vision board with your goals and dreams.'},
            {'category': creative, 'title': 'Learn Origami', 'description': 'Learn to fold a simple origami figure.'},
            {'category': creative, 'title': 'Design a T-Shirt', 'description': 'Create a design for a t-shirt you would wear.'},
            {'category': creative, 'title': 'Write a Song Lyric', 'description': 'Write lyrics for a song about anything you choose.'},
            {'category': creative, 'title': 'Make a Time Capsule', 'description': 'Create a small time capsule with items representing today.'},
            {'category': creative, 'title': 'Draw Your Dream House', 'description': 'Sketch a floor plan or drawing of your dream house.'},

            # === Social Challenges ===
            # These challenges promote building connections, empathy, and positive interactions with others.
            {'category': social, 'title': 'Call a Friend or Family Member', 'description': 'Have a meaningful conversation with someone you care about over the phone.'},
            {'category': social, 'title': 'Compliment a Stranger', 'description': 'Give a genuine compliment to someone you don\'t know.'},
            {'category': social, 'title': 'Perform a Random Act of Kindness', 'description': 'Do something nice for someone without expecting anything in return.'},
            {'category': social, 'title': 'Message an Old Friend', 'description': 'Reach out to an old friend you haven\'t spoken to in a while.'},
            {'category': social, 'title': 'Leave a Positive Comment', 'description': 'Leave a positive and encouraging comment on a social media post or a blog.'},
            {'category': social, 'title': 'Ask Someone About Their Day', 'description': 'Engage in a conversation and actively listen to how someone\'s day went.'},
            {'category': social, 'title': 'Help a Neighbor', 'description': 'Offer to help a neighbor with a small task (e.g., carrying groceries).'},
            {'category': social, 'title': 'Share a Useful Resource', 'description': 'Share an article, video, or tool you found helpful with someone in your network.'},
            {'category': social, 'title': 'Express Gratitude', 'description': 'Tell someone in person how much you appreciate them.'},
            {'category': social, 'title': 'Volunteer for an Hour', 'description': 'Spend one hour volunteering for a cause you care about (online or in-person).'},
            {'category': social, 'title': 'Donate Unused Items', 'description': 'Donate clothes, books, or other items you no longer need.'},
            {'category': social, 'title': 'Give Up Your Seat', 'description': 'Give up your seat on public transport to someone who needs it more.'},
            {'category': social, 'title': 'Send Thank You Notes', 'description': 'Write and send thank you notes to 3 people who have helped you.'},
            {'category': social, 'title': 'Start a Conversation', 'description': 'Start a conversation with a colleague or classmate about their interests.'},
            {'category': social, 'title': 'Share a Meal', 'description': 'Invite someone to share a meal with you (in person or virtually).'},
            {'category': social, 'title': 'Mentor Someone', 'description': 'Offer to mentor or help someone with a skill you possess.'},
            {'category': social, 'title': 'Organize a Game Night', 'description': 'Plan and host a virtual or in-person game night with friends.'},
            {'category': social, 'title': 'Create a Community Group', 'description': 'Start a small community group or club for people with shared interests.'},
            {'category': social, 'title': 'Support a Local Business', 'description': 'Leave a positive review for a local business you like.'},
            {'category': social, 'title': 'Practice Active Listening', 'description': 'Have a conversation where you focus entirely on listening without interrupting.'},

            # === Mindfulness Challenges ===
            # These challenges help you develop awareness, reduce stress, and cultivate a sense of presence and gratitude.
            {'category': mindfulness, 'title': '5-Minute Meditation', 'description': 'Sit in a quiet place and focus on your breath for five minutes.'},
            {'category': mindfulness, 'title': 'Digital Detox', 'description': 'Avoid all social media for a two-hour block during the day.'},
            {'category': mindfulness, 'title': 'Mindful Eating', 'description': 'Eat one meal without any distractions (no phone, no TV) and focus on the food.'},
            {'category': mindfulness, 'title': 'Gratitude List', 'description': 'Write down three things you are grateful for today.'},
            {'category': mindfulness, 'title': 'Observe Your Surroundings', 'description': 'Spend 5 minutes just observing your environment, noticing details you usually miss.'},
            {'category': mindfulness, 'title': 'Body Scan Meditation', 'description': 'Do a 10-minute body scan meditation, focusing on each part of your body.'},
            {'category': mindfulness, 'title': 'Mindful Breathing Break', 'description': 'Take 3 minutes to focus solely on your breathing, clearing your mind.'},
            {'category': mindfulness, 'title': 'Nature Observation', 'description': 'Spend 10 minutes outdoors, observing nature without using your phone.'},
            {'category': mindfulness, 'title': 'Evening Reflection', 'description': 'Before bed, spend 5 minutes reflecting on the best part of your day.'},
            {'category': mindfulness, 'title': 'Progressive Muscle Relaxation', 'description': 'Tense and relax each muscle group in your body for 5 seconds.'},
            {'category': mindfulness, 'title': 'Mindful Shower', 'description': 'Take a shower focusing entirely on the sensation of water and smell of soap.'},
            {'category': mindfulness, 'title': 'Silent Hour', 'description': 'Spend one hour in complete silence, no talking or electronics.'},
            {'category': mindfulness, 'title': 'Loving-Kindness Meditation', 'description': 'Send love and positive thoughts to yourself and others for 10 minutes.'},
            {'category': mindfulness, 'title': 'Mindful Walking', 'description': 'Take a 10-minute walk focusing on each step and your surroundings.'},
            {'category': mindfulness, 'title': 'Declutter Your Mind', 'description': 'Write down all your worries and thoughts, then tear the paper up.'},
            {'category': mindfulness, 'title': 'Practice Forgiveness', 'description': 'Write a letter (you don\'t have to send it) forgiving someone who hurt you.'},
            {'category': mindfulness, 'title': 'Mindful Journaling', 'description': 'Write for 10 minutes about your current emotional state without judgment.'},
            {'category': mindfulness, 'title': 'Create a Peaceful Space', 'description': 'Designate and organize a small area in your home for relaxation.'},
            {'category': mindfulness, 'title': 'Practice Gratitude for Strangers', 'description': 'Think of 5 things strangers do that make your life better.'},
            {'category': mindfulness, 'title': 'Mindful Tea/Coffee Drinking', 'description': 'Drink a cup of tea or coffee slowly, focusing on taste, warmth, and aroma.'},
        ]

        for data in challenges:
            Challenge.objects.create(
                category=data['category'],
                title=data['title'],
                description=data['description']
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with 100 challenges (20 per category).'))