export const productTypeDef = `
  type Product {
      id: Int!
      name: String!
      description: String!
      unit_measurement: String!
      quantity: Int!
      category: Category!
  }
  input ProductInput {
      name: String!
      description:  String!
      category: Int!
      unit_measurement: String!
      quantity: Int!
      color:  Int!
  }`;

export const productQueries = `
      allProducts: [Product]!
      productById(id: Int!): Product!
  `;

export const productMutations = `
    createProduct(product: ProductInput!): Product!
    updateProduct(id: Int!, product: ProductInput!): Product!
    deleteProduct(id: Int!): Int
`;
