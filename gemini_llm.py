from langchain_google_genai import ChatGoogleGenerativeAI
import os
import sys
from educhain import LLMConfig, Educhain
from dotenv import load_dotenv

load_dotenv()

gemini_flash = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"))

flash_config = LLMConfig(custom_model=gemini_flash)
client = Educhain(flash_config)

def generate_mcqs(topic: str, number_of_questions: int):
    """
    Generate n number of MCQs on given topic.
    :param topic: given topics.
    :param number_of_questions: n number.
    :return: n number of MCQs.
    """
    ques = client.qna_engine.generate_questions(
        topic=topic,
        num=number_of_questions
    )

    return ques.model_dump_json()

def generate_lesson_plan(topic: str):
    """
    Generates lesson plan on given topic
    :param topic: topic on which lesson needs to be generated.
    :return: generated lesson plan on given topic
    """
    try:
        # Suppress stdout to prevent printing
        original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

        lesson_plan = client.content_engine.generate_lesson_plan(topic=topic)

        # Restore stdout
        sys.stdout.close()
        sys.stdout = original_stdout

        return lesson_plan

    except Exception as e:
        # Restore stdout in case of error
        if 'original_stdout' in locals():
            sys.stdout = original_stdout

        return str({
            "error": str(e),
            "title": "",
            "subject": "",
            "learning_objectives": [],
            "lesson_introduction": "",
            "main_topics": "",
            "learning_adaptations": "",
            "real_world_applications": "",
            "ethical_considerations": ""
        })

def generate_different_types_of_question(topic: str,
                                         number_of_questions: int,
                                         question_type: str,
                                         difficulty_level: str
                                         ):
    """
    This function generates different kinds of questions
    :param topic:
    :param number_of_questions:
    :param question_type:
    :param difficulty_level:
    :return:
    """

    ques = client.qna_engine.generate_questions(topic=topic,
                                                num=number_of_questions,
                                                question_type=question_type,
                                                custom_instructions=difficulty_level)

    return ques.model_dump_json()
