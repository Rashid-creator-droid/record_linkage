"""Migration name

Revision ID: 7d5e98ce514d
Revises: f121ed7d630d
Create Date: 2023-11-26 18:44:29.414944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7d5e98ce514d"
down_revision: Union[str, None] = "f121ed7d630d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "dealerprices",
        "product_key",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "dealerprices",
        "price",
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=True,
    )
    op.alter_column(
        "dealerprices",
        "product_url",
        existing_type=sa.VARCHAR(),
        nullable=True,
    )
    op.alter_column(
        "dealerprices",
        "product_name",
        existing_type=sa.VARCHAR(),
        nullable=True,
    )
    op.alter_column(
        "dealerprices", "date", existing_type=sa.DATE(), nullable=True
    )
    op.alter_column(
        "dealerprices", "dealer_id", existing_type=sa.INTEGER(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "dealerprices", "dealer_id", existing_type=sa.INTEGER(), nullable=False
    )
    op.alter_column(
        "dealerprices", "date", existing_type=sa.DATE(), nullable=False
    )
    op.alter_column(
        "dealerprices",
        "product_name",
        existing_type=sa.VARCHAR(),
        nullable=False,
    )
    op.alter_column(
        "dealerprices",
        "product_url",
        existing_type=sa.VARCHAR(),
        nullable=False,
    )
    op.alter_column(
        "dealerprices",
        "price",
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=False,
    )
    op.alter_column(
        "dealerprices",
        "product_key",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    # ### end Alembic commands ###