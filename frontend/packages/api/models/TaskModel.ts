/* tslint:disable */
/* eslint-disable */
/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface TaskModel
 */
export interface TaskModel {
    /**
     * 
     * @type {string}
     * @memberof TaskModel
     */
    id: string;
    /**
     * 
     * @type {string}
     * @memberof TaskModel
     */
    name: string;
    /**
     * 
     * @type {Date}
     * @memberof TaskModel
     */
    completed: Date | null;
}

/**
 * Check if a given object implements the TaskModel interface.
 */
export function instanceOfTaskModel(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "id" in value;
    isInstance = isInstance && "name" in value;
    isInstance = isInstance && "completed" in value;

    return isInstance;
}

export function TaskModelFromJSON(json: any): TaskModel {
    return TaskModelFromJSONTyped(json, false);
}

export function TaskModelFromJSONTyped(json: any, ignoreDiscriminator: boolean): TaskModel {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'name': json['name'],
        'completed': (json['completed'] === null ? null : new Date(json['completed'])),
    };
}

export function TaskModelToJSON(value?: TaskModel | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'name': value.name,
        'completed': (value.completed === null ? null : value.completed.toISOString()),
    };
}
