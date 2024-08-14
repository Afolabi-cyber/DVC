from pydantic import BaseModel

class Water(BaseModel):
    ph: float
    hardness: float
    Solids: float
    Chloramines : float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float