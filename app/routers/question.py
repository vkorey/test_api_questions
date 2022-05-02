from fastapi import APIRouter

router = APIRouter()


@router.post('/question')
async def question(questions_num: int,):
    return {'question': questions_num}
