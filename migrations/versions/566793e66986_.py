"""empty message

Revision ID: 566793e66986
Revises: 4ee18d0b8a6f
Create Date: 2018-09-30 18:36:41.803220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '566793e66986'
down_revision = '4ee18d0b8a6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('active', sa.Integer(), nullable=True))
    op.add_column('item', sa.Column('barcode', sa.String(length=255), nullable=True))
    op.add_column('item', sa.Column('class_', sa.String(length=50), nullable=True))
    op.add_column('item', sa.Column('image', sa.String(length=50), nullable=True))
    op.add_column('item', sa.Column('type_', sa.Integer(), nullable=True))
    op.add_column('item', sa.Column('uom', sa.String(length=20), nullable=True))
    op.add_column('lot', sa.Column('bin_', sa.String(length=10), nullable=True))
    op.add_column('lot', sa.Column('exp_date', sa.DateTime(), nullable=True))
    op.add_column('lot', sa.Column('item', sa.String(length=60), nullable=True))
    op.add_column('lot', sa.Column('qty_', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lot', 'qty_')
    op.drop_column('lot', 'item')
    op.drop_column('lot', 'exp_date')
    op.drop_column('lot', 'bin_')
    op.drop_column('item', 'uom')
    op.drop_column('item', 'type_')
    op.drop_column('item', 'image')
    op.drop_column('item', 'class_')
    op.drop_column('item', 'barcode')
    op.drop_column('item', 'active')
    # ### end Alembic commands ###
