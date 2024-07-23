function apiError(msg, code) {
    throw { message: msg, apiCode: code };
}
console.log(apiError("Server Side Error", 100));
