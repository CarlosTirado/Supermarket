import merge from 'lodash.merge';
import GraphQLJSON from 'graphql-type-json';
import { makeExecutableSchema } from 'graphql-tools';

import { mergeSchemas } from './utilities';

import {
	categoryMutations,
	categoryQueries,
	categoryTypeDef
} from './supermarket/categories/typeDefs';

import categoryResolvers from './supermarket/categories/resolvers';

import {
	productMutations,
	productQueries,
	productTypeDef
} from './supermarket/products/typeDefs';

import productResolvers from './supermarket/products/resolvers';

import {
	userMutations,
	userQueries,
	userTypeDef
} from './users/user/typeDefs';

import userResolvers from './users/user/resolvers';

// merge the typeDefs
const mergedTypeDefs = mergeSchemas(
	[
		'scalar JSON',
		categoryTypeDef,
		productTypeDef,
		userTypeDef
	],
	[
		categoryQueries,
		productQueries,
		userQueries
	],
	[
		categoryMutations,
		productMutations,
		userMutations
	]
);

// Generate the schema object from your types definition.
export default makeExecutableSchema({
	typeDefs: mergedTypeDefs,
	resolvers: merge(
		{ JSON: GraphQLJSON }, // allows scalar JSON
		categoryResolvers,
		productResolvers,
		userResolvers
	)
});
