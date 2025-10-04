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

I would like to come up with a test set that I can use to evaluate my RAG system.

I would like to test both my RAG retrieval and my question answering.

STRATEGY FOR EVALUATION

I would like to curate some sample questions, such as:

Who won the prestigious IIOTY award in 2023?

For each question, I would have key words that must be in the retrieved context:

Maxine, Thompson, Innovator

And for each question, I would have a Reference Answer:

Maxine Thompson won the prestigious Insurellm Innovator of the Year (IIOTY) award in 2023.

METRICS

I will then calculate a number of metrics:

1. For RAG retrieval, measure MRR and nDCG
2. For question answering, measure % of key words included, and also use an LLM-as-a-judge with structured outputs:
{
    "feedback": "your thoughts on the answer",
    "accuracy 1-5": 5,
    "completeness 1-5": 5,
    "relevance 1-5": 5
}
3. Also some adversarial testing that it does not invent answers to questions not in context

Your actions:

Please review all the documents and generate 100 test questions based on them!

Create a jsonl document week2/tests.jsonl where each line is a test:

{"question": "Who won the IIOTY award in 2023", "keywords": ["Maxine", "Thompson", "innovator"], "reference_answer": "Maxine Thompson won the prestigious Insurellm Innovator of the Year (IIOTY) award in 2023", "category": "direct_fact"}

QUESTION CATEGORIES:

Current categories in use:
- `direct_fact`: Direct factual retrieval questions that can be answered from a single document
- `temporal`: Questions involving dates, sequences, or time-based information
- `comparative`: Questions comparing different products, policies, people, or entities
- `numerical`: Questions involving specific numbers, quantities, or statistics
- `relationship`: Questions about organizational relationships, hierarchies, or connections between entities

Future categories (not yet implemented):
- `negative`: Questions that have no answer in the knowledge base
- `adversarial`: Off-topic questions designed to test if the system stays within bounds
- `spanning`: Questions that require information from multiple documents
- `holistic`: Questions requiring broader understanding across multiple contexts

You can find useful questions from the existing knowledge-base docs, being sure to take examples from all subdirectories. Do not change the knowledge base; try to take existing facts. Have a broad range of different kinds of retrieval so that the RAG process is thoroughly tested. For now, focus on each question being answered in 1 document; avoid questions that require context from multiple documents.





