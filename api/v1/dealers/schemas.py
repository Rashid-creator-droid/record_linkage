from pydantic import BaseModel, ConfigDict, AnyUrl
from datetime import date

from api.v1.products.schemas import ProductSmall


class ProductDealerPrice(BaseModel):
    status: bool | None
    product: ProductSmall | None


class Dealer(BaseModel):
    id: int
    name: str


class DealerPriceBase(BaseModel):
    id: int
    product_key: int | None
    price: float | None
    product_url: AnyUrl | None
    product_name: str | None
    date: date

    class Config:
        json_encoders = {date: lambda v: v.strftime("%d.%m.%Y")}


class DealerPrice(DealerPriceBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class DealerPriceView(DealerPrice):
    dealer: Dealer
    productdealer: ProductDealerPrice | None
