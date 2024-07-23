function apiError(msg: string, code: number): never {

    throw { message: msg, apiCode: code }

}
console.log(apiError("Server Side Error", 100));
