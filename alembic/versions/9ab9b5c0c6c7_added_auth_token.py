"""added auth token

Revision ID: 9ab9b5c0c6c7
Revises: c243403b3c94
Create Date: 2023-07-12 15:37:28.734516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ab9b5c0c6c7'
down_revision = 'c243403b3c94'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('access_token', sa.String(), nullable=False),
    sa.Column('refresh_token', sa.String(), nullable=False),
    sa.Column('access_token_expires_at', sa.DateTime(), nullable=False),
    sa.Column('refresh_token_expires_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['public.user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_token_access_token'), 'token', ['access_token'], unique=True, schema='public')
    op.create_index(op.f('ix_public_token_refresh_token'), 'token', ['refresh_token'], unique=True, schema='public')
    op.drop_constraint('user_status_code_fkey', 'user', type_='foreignkey')
    op.create_foreign_key(None, 'user', 'user_status', ['status_code'], ['code'], source_schema='public', referent_schema='public')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', schema='public', type_='foreignkey')
    op.create_foreign_key('user_status_code_fkey', 'user', 'user_status', ['status_code'], ['code'])
    op.drop_index(op.f('ix_public_token_refresh_token'), table_name='token', schema='public')
    op.drop_index(op.f('ix_public_token_access_token'), table_name='token', schema='public')
    op.drop_table('token', schema='public')
    # ### end Alembic commands ###
