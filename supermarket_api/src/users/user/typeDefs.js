export const userTypeDef = `
	type User {
		id: Int!
		username: String!
		password: String!
	}
	input UserInput {
		username: String!
		password: String!
	}`;

export const userQueries = `
	userByUsernameAndPassword(username: String!, password: String!): User!
`;

export const userMutations = `
	createUser(user: UserInput!): User!
`;
