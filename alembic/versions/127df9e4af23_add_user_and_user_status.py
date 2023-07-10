"""Add user and user status

Revision ID: 127df9e4af23
Revises: 
Create Date: 2023-07-10 10:07:38.942941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '127df9e4af23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_statuses',
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('label', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('code'),
    schema='public'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_statuses', schema='public')
    # ### end Alembic commands ###
