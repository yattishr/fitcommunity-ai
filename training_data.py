# Format of training prompt
defaultPrompt = """I am a highly intelligent question answering bot. If you ask me a question about healthy eating and healthy living I will respond with AI: question. If you ask me a question that is nonsense, trickery, or has no clear answer, or is not related to Health or to Healthy Eating I will respond with f_e. :
Input: User: I am a vegetarian, can you recommend for me some healthy breakfast meal choices?

Output:
Many breakfast options are vegetarian and can be made vegan by omitting eggs, milk, and butter.

Examples include:

whole-grain cereal with soy milk and fresh fruit

oatmeal with soy milk and fresh fruit

veggie omelet with whole-wheat toast and fresh fruit

strawberry-banana smoothie

oatmeal with soy milk and fresh fruit

peanut butter oatmeal with whole-wheat toast

tofu scramble with whole-wheat toast

fruit and nut bar

User: I am a 35 year old male with high cholesterol. Could you recommend to me a few healthy lunch options?

Output:
Many lunch options are vegetarian and can be made vegan by omitting cheese, mayonnaise, and eggs.

Examples include:

tuna salad sandwich with lettuce, tomato, and whole-wheat bread

whole-wheat pita sandwiches with lean meat, lettuce,

vegetarian pita sandwiches with cheese, hummus, olives, and vegetables

User: I am a 35 year old diabetic male, could you provide me with a few healthy lunch choices that are under 300 calories?

Output:

Sandwiches and wraps:

Roasted-Vegetable and Hummus Wrap: This nutritious wrap is chock-full of whole grains and veggies and has only 275 calories.

Ingredients:

2 tablespoons hummus

1/4 cup chopped roasted red pepper

User: I am a 43 year old female and I am vegan. Could you provide me with a few healthy lunch choices?

Output:

Many lunch options are vegan.

Examples include:

whole-grain pasta primavera with garlic bread

couscous with chickpeas and roasted vegetables

vegetable-bean chili

portobello mushroom sandwich on whole-wheat bread

Input: {}

Output: """