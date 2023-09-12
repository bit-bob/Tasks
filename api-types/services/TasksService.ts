/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class TasksService {

    /**
     * Add Task
     * @param name
     * @returns any Successful Response
     * @throws ApiError
     */
    public static addTask(
        name: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/tasks',
            query: {
                'name': name,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Tasks
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getTasks(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/tasks',
        });
    }

    /**
     * Update Task
     * @param taskId
     * @param name
     * @returns any Successful Response
     * @throws ApiError
     */
    public static updateTask(
        taskId: number,
        name: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/tasks/update',
            query: {
                'task_id': taskId,
                'name': name,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Play Task
     * @param taskId
     * @param timeIsoString
     * @returns any Successful Response
     * @throws ApiError
     */
    public static playTask(
        taskId: number,
        timeIsoString: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/tasks/play',
            query: {
                'task_id': taskId,
                'time_iso_string': timeIsoString,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Pause Task
     * @param taskId
     * @param timeIsoString
     * @returns any Successful Response
     * @throws ApiError
     */
    public static pauseTask(
        taskId: number,
        timeIsoString: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/tasks/pause',
            query: {
                'task_id': taskId,
                'time_iso_string': timeIsoString,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
