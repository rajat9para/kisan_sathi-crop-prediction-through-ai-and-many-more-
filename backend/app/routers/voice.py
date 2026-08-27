from fastapi import APIRouter
from app.models.schemas import VoiceQueryRequest, VoiceQueryResponse
from app.services.llm_advisor import llm_advisor

router = APIRouter(prefix="/api/voice", tags=["Voice Saathi"])

@router.post("/query", response_model=VoiceQueryResponse)
async def handle_voice_query(req: VoiceQueryRequest):
    """
    NLP Intent Classifier and Conversational Engine for Voice Saathi.
    Uses Groq LLaMA 3.3 for grounded conversational reasoning in Hindi/English,
    with instant local fallback.
    """
    res = llm_advisor.answer_farmer_voice_query(
        query_text=req.query_text,
        language=req.language or "hi",
        crop_context=req.crop_context or "General Crop",
        location=req.location_context or "Nashik, Maharashtra"
    )
    return res
