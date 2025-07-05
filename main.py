from mcp.server.fastmcp import FastMCP
from gemini_llm import generate_mcqs, generate_lesson_plan, generate_different_types_of_question

mcp = FastMCP("Educahin AI Learning Companion")


@mcp.tool()
def generate_mcqs_from_educhain(topic,
                                number_of_questions
                                ):
    """
    This function is used to generate desired number MCQ questions on given topic
    :param topic: topic on which the user wants question to be generated.
    :param number_of_questions: number of question required for the given topic.
    :return:
    {
        "questions": [
            {
                "question": "string - The question text",
                "answer": "string - The correct answer (must match one of the options)",
                "explanation": "string - Detailed explanation of the correct answer",
                "options": [
                    "string - Option 1",
                    "string - Option 2",
                    "string - Option 3",
                    "string - Option 4"
                ]
            }
        ]
    }
    """

    ques = generate_mcqs(
        topic=topic,
        number_of_questions=number_of_questions
    )

    return ques


@mcp.tool()
def generate_lesson_plan_from_educhain(topic: str):
    """
    This function creates lesson plan on given topic.
    :param topic: Topic on which the user wants to create the lesson plan
    :return:
    {
      "title": "string",
      "subject": "string",
      "learning_objectives": ["string", "string", ...],
      "lesson_introduction": "string",
      "main_topics": [MainTopic, MainTopic, ...],
      "learning_adaptations": "string",
      "real_world_applications": "string",
      "ethical_considerations": "string"
    }
    """

    lesson_plan = generate_lesson_plan(
        topic=topic
    )

    return lesson_plan

@mcp.tool()
def generate_different_types_of_question_from_educhain(
        topic: str,
        number_of_questions: int,
        question_type: str,
        difficulty_level: str
        ):
    """
    This function generates different kinds of questions with educhian SDK
    :param topic: topic of the question
    :param number_of_questions: number of the question needs to be generated
    :param question_type: "True/False", "Fill in the Blank", or "Short Answer"
    :param difficulty_level: easy, medium, or hard
    :return: requested number of qustions of given type and difficulty
    """
    ques = generate_different_types_of_question(topic=topic,
                                                number_of_questions=number_of_questions,
                                                question_type=question_type,
                                                difficulty_level=difficulty_level)

    return ques


if __name__ == "__main__":
    mcp.run(transport='stdio')
