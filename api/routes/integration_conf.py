from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.config import settings

router = APIRouter()


integration_json = {
    "data": {
        "date": {"created_at": "2025-02-13", "updated_at": "2025-02-13"},
        "descriptions": {
            "app_name": "telex-ci-cd",
            "app_description": "a simple ci/cd slack notifier application",
            "app_logo": "http://ec2-13-60-216-247.eu-north-1.compute.amazonaws.com",
            "app_url": "http://ec2-13-60-216-247.eu-north-1.compute.amazonaws.com",
            "background_color": "#fff",
        },
        "is_active": True,
        "integration_type": "modifier",
        "key_features": ["real time updates", "slack notifcation"],
        "author": "Darasimi",
        "settings": [
            {
                "label": "slack-channel",
                "type": "text",
                "required": True,
                "default": "#DevopsAlert",
            },
            {
                "label": "time interval",
                "type": "dropdown",
                "required": True,
                "default": "immediate",
                "options": ["immediate", "Every 5-min", "Every 10-min", "Every 1-hour"],
            },
            {
                "label": "event type",
                "type": "dropdown",
                "required": True,
                "default": "ci_pipeline",
                "options": ["ci_pipeline", "cd_pipeline", "deployment", "error"],
            },
            {"label": "message", "type": "text", "required": True, "default": "Basic"},
            {
                "label": "include logs",
                "type": "checkbox",
                "required": True,
                "default": "true",
            },
        ],
        "target_url": settings.SLACK_WEBHOOK_URL,
        "tick_url": settings.TICK_URL,
    }
}


@router.get("/integration-config")
async def get_integration_json():
    return JSONResponse(content=integration_json)
