def main():
    from rdkit import Chem
    mol = Chem.MolFromSmiles('CCO')
    return Chem.MolToMolBlock(mol)

# Export the `main` function
__pragma__('js', '{}', """
export { main };
""")