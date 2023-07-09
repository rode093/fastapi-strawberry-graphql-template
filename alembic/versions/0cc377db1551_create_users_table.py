"""create users table

Revision ID: 0cc377db1551
Revises:
Create Date: 2023-07-09 15:01:28.627961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cc377db1551'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.UUID, primary_key=True,
                  server_default=sa.text("gen_random_uuid()")),
        sa.Column('first_name', sa.String(64), nullable=False),
        sa.Column('last_name', sa.String(64), nullable=False),
        sa.Column('email', sa.String(64), nullable=False),
        sa.Column('password', sa.String(512), nullable=False),
        sa.Column('reset_token', sa.String(512), nullable=True),
        sa.Column('status', sa.String(16), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True),
                  server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('users')
