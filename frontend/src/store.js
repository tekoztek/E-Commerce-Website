import { configureStore, combineReducers } from '@reduxjs/toolkit'
import { thunk } from 'redux-thunk'
import { productListReducer } from './reducers/productReducers'


const reducer = combineReducers({
    productList: productListReducer,
})

const store = configureStore({
    reducer,
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
});

export default store