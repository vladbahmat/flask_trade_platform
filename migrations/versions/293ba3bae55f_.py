"""empty message

Revision ID: 293ba3bae55f
Revises: 1c067ac60f98
Create Date: 2021-06-01 10:03:26.917609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '293ba3bae55f'
down_revision = '1c067ac60f98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('offer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.DECIMAL(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_sell', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.Column('buyer_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('seller_offer_id', sa.Integer(), nullable=True),
    sa.Column('buyer_offer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['buyer_id'], ['profile.id'], ),
    sa.ForeignKeyConstraint(['buyer_offer_id'], ['offer.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['seller_id'], ['profile.id'], ),
    sa.ForeignKeyConstraint(['seller_offer_id'], ['offer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trade')
    op.drop_table('offer')
    op.drop_table('inventory')
    # ### end Alembic commands ###