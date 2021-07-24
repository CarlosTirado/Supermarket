export const userTypeDef = `
	type User {
		id: Int!
		user: String!
		password: String!
	}
	input UserInput {
		user: String!
		password: String!
	}`;

export const userQueries = `
	userByUsernameAndPassword(username: String!, password: String!): User!
`;

export const userMutations = `
	createUser(user: UserInput!): User!
`;
