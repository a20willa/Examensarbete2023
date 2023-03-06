export interface connection_strings_mysql {
    // MySQL
    host: string,
    user: string,
    user_password: string,
    database: string,
    port: number,
    table_name?: string,
}
export interface connection_strings_mongodb {
    // MongoDB
    host: string,
    database: string,
    collection_name: string
}