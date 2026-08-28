"""
Plant Doctor & Leaf Disease Pathology Router
Accepts leaf image uploads (base64 or multipart), extracts visual necrotic pathology signatures,
and runs the disease classifier with live weather spray alerts and organic/chemical remedies.
"""

from fastapi import APIRouter, File, UploadFile, Form
from typing import Optional
import base64
from pydantic import BaseModel
from app.services.disease_classifier import disease_classifier

router = APIRouter(prefix="/api/doctor", tags=["Plant Doctor & Leaf Pathology"])

class DiagnoseJsonRequest(BaseModel):
    image_base64: Optional[str] = None
    crop_hint: Optional[str] = None
    language: Optional[str] = "hi"
    preset_sample: Optional[str] = None

@router.post("/diagnose")
async def diagnose_leaf_disease(req: DiagnoseJsonRequest):
    """
    Diagnoses plant disease from Base64 leaf image string or preset sample.
    """
    image_bytes = b""
    if req.image_base64:
        try:
            # Strip data:image/...;base64, header if present
            raw_b64 = req.image_base64.split(",")[-1]
            image_bytes = base64.b64decode(raw_b64)
        except Exception:
            image_bytes = b""
            
    result = disease_classifier.diagnose_image(
        image_bytes=image_bytes,
        crop_hint=req.crop_hint or req.preset_sample,
        language=req.language or "hi"
    )
    return result

@router.post("/diagnose-file")
async def diagnose_leaf_file(
    file: UploadFile = File(...),
    crop_hint: Optional[str] = Form(None),
    language: Optional[str] = Form("hi")
):
    """
    Diagnoses plant disease from uploaded leaf image file.
    """
    contents = await file.read()
    result = disease_classifier.diagnose_image(
        image_bytes=contents,
        crop_hint=crop_hint,
        language=language or "hi"
    )
    return result
