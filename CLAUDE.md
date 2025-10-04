This is a repo to be used for students on the SuperDataScience (SDS) AI Bootcamp.

We are working to prepare the materials for Week 2 if the bootcamp, in the week2 folder.

The full path to the project root is:
/Users/ed/projects/sds/

The week2 folder is:
/Users/ed/projects/sds/week2

The week is all about RAG.

In this folder is synthetic data about a fictional company, Insurellm.

Please read all the files in knowledge-base/company/ to learn about the company.

Also review the list of files in the other knowledge-base subdirectories.

The goal is to test both RAG retrieval and question answering.

STRATEGY FOR EVALUATION

We have curated test questions such as:  
Who won the prestigious IIOTY award in 2023?

For each question, we have identified key words that must be in the retrieved context:  
Maxine, Thompson, Innovator

And for each question, we have a Reference Answer:  
Maxine Thompson won the prestigious Insurellm Innovator of the Year (IIOTY) award in 2023.

METRICS

We will calculate a number of metrics:

1. For RAG retrieval, measure MRR and nDCG
2. For question answering, measure % of key words included, and also use an LLM-as-a-judge with structured outputs:
{
    "feedback": "your thoughts on the answer",
    "accuracy 1-5": 5,
    "completeness 1-5": 5,
    "relevance 1-5": 5
}
3. Also some adversarial testing that it does not invent answers to questions not in context

The test dataset week2/tests.jsonl has been fully populated with 150 questions.

QUESTION CATEGORIES & COUNTS:

Active categories (150 questions total):
- `direct_fact`: 70 questions - Direct factual retrieval questions that can be answered from a single document
- `spanning`: 20 questions - Questions that require information from exactly 2 different documents
- `temporal`: 20 questions - Questions involving dates, sequences, or time-based information
- `comparative`: 10 questions - Questions comparing different products, policies, people, or entities
- `numerical`: 10 questions - Questions involving specific numbers, quantities, or statistics
- `relationship`: 10 questions - Questions about organizational relationships, hierarchies, or connections between entities
- `holistic`: 10 questions - Broad questions requiring aggregation or understanding across many documents (intentionally challenging for basic RAG)

Future categories (not yet implemented):
- `negative`: Questions that have no answer in the knowledge base
- `adversarial`: Off-topic questions designed to test if the system stays within bounds

JSONL FORMAT:

Each line in tests.jsonl follows this format:
{"question": "Who won the IIOTY award in 2023", "keywords": ["Maxine", "Thompson", "IIOTY"], "reference_answer": "Maxine Thompson won the prestigious Insurellm Innovator of the Year (IIOTY) award in 2023", "category": "direct_fact"}

IMPORTANT NOTES ON KEYWORDS:

1. Keywords are EXACT strings that appear in the source documents
2. Keywords are MINIMAL - only critical terms needed for retrieval (typically 2-3 keywords)
3. Keywords are designed to test if the RAG system retrieves the correct document chunk
4. For holistic questions, keywords are intentionally minimal since these questions require broad context
5. All keywords have been verified against actual source documents in week2/knowledge-base/

DATASET COVERAGE:

The 150 questions cover all subdirectories in the knowledge base:
- company/ (founding, vision, values, office locations, employee counts)
- products/ (all 8 products: Carllm, Homellm, Lifellm, Healthllm, Bizllm, Markellm, Claimllm, Rellm)
- contracts/ (32 contracts across all product lines)
- employees/ (32 employees with various roles, salaries, locations, achievements)

TESTING STRATEGY:

The dataset tests multiple retrieval challenges:
- Single-document retrieval (direct_fact, temporal, comparative, numerical, relationship)
- Multi-document retrieval (spanning - requires 2 docs)
- Broad aggregation/understanding (holistic - requires many docs or reasoning)

This comprehensive test set enables evaluation of:
1. RAG retrieval accuracy (MRR, nDCG) - using keywords to verify correct chunks retrieved
2. Question answering quality (LLM-as-a-judge with accuracy/completeness/relevance scores)
3. Multi-document synthesis capabilities (spanning questions)
4. Advanced reasoning capabilities (holistic questions)

ACTION PLAN FOR THE PROJECT

Please carefully read these modules which are working great:
week2/ingest.py
week2/app.py

Then we need to do this:

1. Write test.py to have a Pydantic object for the test data in tests.jsonl, and a load_tests that loads them all in from tests.jsonl
2. Write eval.py with:

- A pydantic object RetrievalEval that has MRR, nDCG, and any other key metrics from a retrieval test
- A pydantic object AnswerEval that has feedback, accuracy, completeness, relevance, with Field descriptions
- A function evaluate_retrieval(test) that gets the top 10 chunks and calculates a RetrievalEval

And a main function that allows us to call this from the command line and specify a test row number, and it will print the retrieval eval for that test number.


